from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from JobSearch.routers import users, authentication
from JobSearch.routers import jobs

app = FastAPI()


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "This is Ramped JobSearch App Backend. Please navigate to /docs to see the API endpoints exposed by the app."}

app.include_router(authentication.router)

app.include_router(users.router)

app.include_router(jobs.router)


from fastapi import APIRouter, Depends, HTTPException, status
from JobSearch import jwttoken
from JobSearch.hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm
from JobSearch import database

router = APIRouter(
    tags=['Authentication']
)


@router.post('/login')
async def login(request: OAuth2PasswordRequestForm = Depends()):

    collection = database.db['_users']

    user = collection.find_one({"email": request.username}, {'_id': 0})

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="The given email doesn't exist.")
    else:
        if not Hash.verify(user['password'], request.password):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect Password")

    # generate a JWT token and return

    access_token = jwttoken.create_access_token(data={"sub": user['email']})

    return {"access_token": access_token, "token_type": "bearer"}

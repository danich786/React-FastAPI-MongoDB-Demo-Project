from fastapi import APIRouter, Depends
from JobSearch import schemas, database, oauth2
from JobSearch import database

router = APIRouter(
    prefix="/search",
    tags=['Jobs']
)


@router.get("/")
def search_job_by_title(title: str, current_user: schemas.User = Depends(oauth2.get_current_user)):

    collection = database.db['_JobPosts']

    collection.create_index(
        [
            ("name_ngrams", "text"),
        ],
        name="job_search_ngrams",
        weights={
            "name_ngrams": 100,
        }
    )

    result = collection.find(
        {
            "$text": {
                "$search": title
            }
        },
        {
            "_id": False,
            "job_name": True,
            "company_name": True,
            "job_full_text": True,
            "post_url": True,
            "post_apply_url": True,
            "company_url": True,
            "company_industry": True,
            "minimum_compensation": True,
            "maximum_compensation": True,
            "compensation_type": True,
            "job_hours": True,
            "role_seniority": True,
            "minimum_education": True,
            "office_location": True,
            "post_html": True,
            "city": True,
            "region": True,
            "country": True,
            "job_published_at": True,
            "last_indexed": True,
        },
    )

    return list(result)

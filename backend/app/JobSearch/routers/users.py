from fastapi import APIRouter, Depends, HTTPException, status
from JobSearch import schemas, database, oauth2
from JobSearch.hashing import Hash
import uuid


router = APIRouter(
    prefix="/user",
    tags=['Users']
)


@router.post('/', response_model=schemas.ShowUser)
def create_new_user(request: schemas.User):

    new_user = {
        'user_id': str(uuid.uuid4()),
        'name': request.name,
        'email': request.email,
        'password': Hash.bcrypt(request.password),
    }

    collection = database.db['_users']
    collection.insert_one(new_user)
    return new_user


@router.get('/')
def get_user_by_email(email: str, current_user: schemas.User = Depends(oauth2.get_current_user)):

    collection = database.db['_users']

    user = collection.find_one({"email": email}, {'_id': 0, 'password': 0})

    if user is not None:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f' User with email {email} not found')


@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(email: str, current_user: schemas.User = Depends(oauth2.get_current_user)):

    collection = database.db['_users']

    collection.delete_one({"email": email})

    return {"message": "User is deleted"}

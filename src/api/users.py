from typing import List

from fastapi import APIRouter, HTTPException

from api import crud
from api.models import UserDB, User, UpdateUserPass, SearchUser
from asyncpg.exceptions import UniqueViolationError

router = APIRouter()



@router.post("/create-user")
async def create_user(user: User):
    try:
        user_id = await crud.post(user)
    except UniqueViolationError as e:
        if bool(str(e).count("email")):
            raise HTTPException(status_code=409, detail="This email is already exists.")
        else:
            raise HTTPException(status_code=409, detail="This username is already exists.")

    response_user = user.dict()
    response_user["id"] = user_id
    return response_user


@router.put("/update-password")
async def change_password(user: UpdateUserPass):
    have_user = bool(await crud.get(user.id))
    if not have_user:
        raise HTTPException(status_code=404, detail="User not found")

    await crud.put(user.id, user.password)
    return True


@router.delete("/delete-user/{user_id}")
async def delete_user(user_id: int):
    user = await crud.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    await crud.delete_user(user_id)

    return user


@router.get("/get-user-list", response_model=List[UserDB])
async def read_all_notes():
    return await crud.get_all()


@router.post("/search")
async def search_user(user: SearchUser):
    user_dict = {}

    for key in user.dict().keys():
        if user.dict()[key]:
            user_dict[key] = user.dict()[key]

    return await crud.search(user_dict)

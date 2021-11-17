from sqlalchemy import select, update, delete, insert

from api.models import User
from database import database
from database.models import Users


async def post(payload: User):
    query = insert(Users).values(username=payload.username, email=payload.email, password=payload.password)
    return await database.execute(query=query)


async def get(id: int):
    query = select(Users).where(id == Users.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = select(Users)
    return await database.fetch_all(query=query)


async def search(user: dict):
    query = select(Users)
    for attr, value in user.items():
        query = query.filter(getattr(Users, attr).like("%%%s%%" % value))
    return await database.fetch_all(query=query)


async def put(user_id: int, password: str):
    query = update(Users).where(user_id == Users.id) \
        .values(password=password).returning(Users.id)
    return await database.execute(query=query)


async def delete_user(id: int):
    query = delete(Users).where(id == Users.id)
    return await database.execute(query=query)

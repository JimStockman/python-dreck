
from typing import Optional
from fastapi import FastAPI

from user import User
from faker import Faker

from pymongo import MongoClient

# fake = Faker()

# user_list = []

# for i in range(0, 10):
#     user_list.append(User(fake.name(), fake.email()))

# for user in user_list:
#     user.print_info()


app = FastAPI()


client = MongoClient('localhost:27017', username='root', password='root')
db = client.admin


@app.get("/")
def read_root():
    return db.command("serverStatus")


# @app.get("/users/{user_id}")
# def read_item(user_id: int, q: Optional[str] = None):
#     try:
#         return user_list[user_id]
#     except:
#         return {"error": "no match"}

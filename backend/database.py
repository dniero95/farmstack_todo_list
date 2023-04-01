from model import Todo
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

database = client['todo-list-db']

colletion = database.todos

async def fetch_one_todo(title:str):
    document = await colletion.find_one({'title':title})
    return document

async def fetch_all_todos():
    todos = []
    cursor = colletion.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo:Todo):
    document = todo
    result = await colletion.insert_one(document)
    return document

async def update_todo(title:str, todo:Todo):
    print(todo.title)
    print(todo.description)
    await colletion.update_one({'title':title}, {'$set':{'title':todo.title, 'description':todo.description}})
    return await fetch_one_todo(todo.title)

async def remove_todo(title):
    await colletion.delete_one({'title':title})
    return True
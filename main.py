from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from model import Todo
from database import fetch_one_todo, fetch_all_todos, create_todo, update_todo, remove_todo
# create app obj

app = FastAPI()


origins = ['https://localhost:3000']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/')
def read_root():
    return {'message': 'welcome from ToDo list'}

@app.get('/api/todos')
async def get_todos():
    response = await fetch_all_todos()
    return response
@app.get('/api/todo/{title}')
async def get_todos():
    response = await fetch_all_todos()
    return response
@app.post('/api/add/todo')
async def add_todo(todo:Todo):
    pass
@app.put('/api/update/todo/{id}')
async def update_todo(id, data):
    pass
@app.delete('/api/delete/todo/{id}')
async def delete_todos(id):
    pass

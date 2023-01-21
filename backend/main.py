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
@app.get('/api/todo/{title}', response_model=Todo)
async def get_todo_by_title(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f'there is no todo item whit this {title}')

@app.post('/api/add/todo', response_class=Todo)
async def add_todo(todo:Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, 'something went wrong')

@app.put('/api/update/todo/{title}', response_model=Todo)
async def update_todo(title:str, desc:str):
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f'there is no todo item whit this {title}')


@app.delete('/api/delete/todo/{title}')
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return 'succesfully deleted todo item!'
    raise HTTPException(404, f'there is no todo item whit this {title}')

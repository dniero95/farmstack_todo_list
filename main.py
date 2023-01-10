from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from model import Todo

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

@app.get('/todo/{id}')
async def get_todo_by_id(id):
    pass
@app.post('/add/todo')
async def add_todo(todo:Todo):
    pass
@app.put('/update/todo/{id}')
async def update_todo(id, data):
    pass
@app.delete('/delete/todo/{id}')
async def delete_todos(id):
    pass

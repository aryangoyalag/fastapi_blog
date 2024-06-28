from fastapi import FastAPI
from . import database
from .routers import blog,user,authentication

app = FastAPI()

database.init_db()

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)



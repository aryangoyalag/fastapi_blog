from fastapi import APIRouter,Depends,status,HTTPException,Response,Request
from .. import schemas,database,models,hashing
from typing import List
from sqlalchemy.orm import joinedload,Session
from ..repository import user
router = APIRouter(
    tags=['User'],
    prefix='/user'
)
get_db = database.get_db
Hash = hashing.Hash

@router.post('/',response_model=schemas.ShowUser)
def create_user(request:schemas.User,db:Session=Depends(get_db)):
    return user.create_user(request,db)

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db: Session = Depends(get_db)):
    return user.get_user(id,db)
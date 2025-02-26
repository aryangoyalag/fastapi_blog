from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DB_URL = 'sqlite:///./blog.db'
engine = create_engine(SQLALCHEMY_DB_URL,connect_args={"check_same_thread":False})

SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base = declarative_base()

def init_db():
    if not os.path.exists("blog.db"):
        Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

import sys

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from KilluaRobot import DATABASE_URL

def start() -> scoped_session:
    engine = create_engine(DATABASE_URL, client_encoding="utf8")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

BASE = declarative_base()
SESSION = start()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from KilluaRobot import DB_URI


BASE = declarative_base()


def start() -> scoped_session:
    engine = create_engine(DB_URI, echo=True, client_encoding="utf8")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine, checkfirst=True)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


SESSION = start()

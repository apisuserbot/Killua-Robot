import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from KilluaRobot import DB_URI, LOGGER as Unknown


BASE = declarative_base()


def start() -> scoped_session:
    engine = create_engine(DB_URI, echo=True, client_encoding="utf8")
    Unknown.info("[PostgreSQL] Connecting to database...")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine, checkfirst=True)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

try:
    SESSION = start()
except Exception as e:
    Unknown.exception(f'[PostgreSQL] Failed to connect due to {e}')
    exit()
   
Unknown.info("[PostgreSQL] Connection successful, session started.")

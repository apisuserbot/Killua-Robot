import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from KilluaRobot import DATABASE_URL, LOGGER as Unknown


if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

def start() -> scoped_session:
    engine = create_engine(DATABASE_URL, echo=True)
    Unknown.info("[PostgreSQL] Connecting to database...")
    BASE = declarative_base()
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine, checkfirst=True)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

try:
    SESSION = start()
except Exception as e:
    Unknown.exception(f'[PostgreSQL] Failed to connect due to {e}')
    exit()
   
Unknown.info("[PostgreSQL] Connection successful, session started.")

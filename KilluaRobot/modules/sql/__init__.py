import sys

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from KilluaRobot import DATABASE_URL, LOGGER


def start() -> scoped_session:
    engine = create_engine(DATABASE_URL, client_encoding="utf8")
    LOGGER.info("PostgreSQL Connecting to database......")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
try:
    SESSION: scoped_session = start()
except Exception as e:
    LOGGER.exception(f"PostgreSQL Failed to connect due to {e}")
    sys.exit()

LOGGER.info("PostgreSQL Connection successful, session started.")

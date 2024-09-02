import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from config import config

# PostgreSQL configuration
POSTGRES_USER = config.DB_USER
POSTGRES_PASSWORD = config.DB_PASSWORD
POSTGRES_HOST = config.DB_HOST
POSTGRES_PORT = config.DB_PORT
POSTGRES_DB = config.DB_NAME

# SQLAlchemy setup
DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

DATABASE_URL = config.DATABASE_URL
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Raw Database setup

def get_pg_conn():
    conn = psycopg2.connect(
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT
    )
    return conn

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import Generator

# Lee la URL desde variable de entorno, si no existe usa SQLite por defecto
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./ecommerce.db")

# SQLite necesita check_same_thread=False, PostgreSQL no
connect_args = {"check_same_thread": False} if "sqlite" in DATABASE_URL else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

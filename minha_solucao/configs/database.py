from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:appdb2023!@localhost"

engine = create_engine(SQLALCHEMY_DATABASE_URL,pool_pre_ping=False,pool_size=30,max_overflow=10)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db_connection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
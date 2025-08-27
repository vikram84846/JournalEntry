from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base   
from dotenv import load_dotenv
import os
load_dotenv()

try:
    DATABASE_URL = os.getenv("DATABASE_URL")
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
except Exception as e:
    print(f"Error loading environment variables: {e}")

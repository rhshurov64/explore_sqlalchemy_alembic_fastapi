from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()



# Database URL (Replace with your actual database credentials)
DATABASE_URL = os.environ.get("DATABASE_URL")
print(DATABASE_URL)

# Create the synchronous engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for the ORM models
Base = declarative_base()

# Dependency function for FastAPI routes
def get_db():
    """
    Dependency function that provides a database session for requests.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

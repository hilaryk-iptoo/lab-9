from sqlmodel import create_engine, Session, SQLModel
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Create database engine
engine = create_engine(
    DATABASE_URL,
    echo=True
)


# FastAPI database dependency
def get_session():
    with Session(engine) as session:
        yield session


# Create database tables
def create_tables():
    SQLModel.metadata.create_all(engine)
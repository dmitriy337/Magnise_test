import os

from databases import Database
from dotenv import load_dotenv
from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://fastapi_user:fastapi_pass@db:5432/db")

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()

Base = declarative_base()

# databases query builder
database = Database(DATABASE_URL)

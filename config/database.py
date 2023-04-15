from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.main import settings

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL, echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

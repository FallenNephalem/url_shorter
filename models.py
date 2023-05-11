from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dto import UrlCreate
from settings import get_settings

engine = create_engine(get_settings().DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(engine)


class Url(Base):
    __tablename__ = 'url'

    url = Column(String, nullable=False)
    short_url = Column(String, nullable=False, primary_key=True, unique=True, index=True)


def init_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

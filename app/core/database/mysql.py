from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.settings import set_up


config = set_up()
engine = create_engine(
    url=config.get("MYSQL_DATABASE_URL"),
    connect_args={},
    pool_recycle=300,
    pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_mysql():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Boolean
from app.core.database import Base, engine


class Users(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id = Column(String(32), primary_key=True, default=uuid4().hex, index=True)
    username = Column(String(25), unique=True)
    password = Column(String(65), unique=True)
    status = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(bind=engine)

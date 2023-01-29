from uuid import uuid4
from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, String
from app.core.database.mysql import Base, engine


class Users(Base):
    """Model Users
    """

    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id = Column(String(32), primary_key=True, default=uuid4().hex, index=True)
    email = Column(String(75), unique=True)
    username = Column(String(45), unique=True)
    password = Column(String(100), unique=True)
    status = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(bind=engine)

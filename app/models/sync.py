from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, DateTime, String
from app.core.database.mysql import Base, engine


class Syncs(Base):
    """Model Syncs
    """

    __tablename__ = "syncs"
    __table_args__ = {'extend_existing': True}

    id = Column(String(32), primary_key=True, default=uuid4().hex, index=True)
    file = Column(String(32), index=True)
    user_id = Column(String(32), index=True)
    profile_id = Column(String(24))
    created_date = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(bind=engine)

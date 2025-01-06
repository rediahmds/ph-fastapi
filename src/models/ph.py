from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, DateTime
from src.databases.db import Base


class PhModel(Base):
    __tablename__ = "ph"

    id = Column(Integer, primary_key=True)
    ph = Column(Float)
    result = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

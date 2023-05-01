from database import Base
from sqlalchemy import Column, Integer, Text, DateTime
import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(Text, nullable=False)
    last_name = Column(Text, nullable=False)
    email = Column(Text, nullable=False, unique=True)
    username = Column(Text, nullable=False, unique=True)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.now)

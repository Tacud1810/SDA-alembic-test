from database import Base
from sqlalchemy import Column, Integer, Text, ForeignKey

from models.user import User


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    label = Column(Text, nullable=False, unique=True)
    user_id = ForeignKey(User.id, ondelete="CASCADE", onupdate="CASCADE")

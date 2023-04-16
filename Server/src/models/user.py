import datetime

from sqlalchemy import Column, String, Boolean, DateTime, Integer
from sqlalchemy.orm import relationship

from Server.src.models.entity import Entity


class User(Entity):
    __tablename__ = "users"

    email = Column(String, index=True, nullable=False)
    login = Column(String, index=True, nullable=False)
    fullname = Column(String, index=True, nullable=False)
    password = Column(String, nullable=False)
    searchs = relationship("Search")


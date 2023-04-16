import datetime

from sqlalchemy import Column, String, Boolean, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship

from Server.src.models.entity import Entity


class Search(Entity):
    __tablename__ = "searches"

    result = Column(String, index=True, nullable=False)
    is_attack = Column(Boolean, nullable=False, default=False)
    type = Column(Integer, ForeignKey("attack.id"), index=True)
    person = Column(Integer, ForeignKey("users.id"), index=True)

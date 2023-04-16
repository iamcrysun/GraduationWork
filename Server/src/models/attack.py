import datetime

from sqlalchemy import Column, String, Boolean, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship

from Server.src.models.entity import Entity


class Attack(Entity):
    __tablename__ = "attacks"

    type = Column(String, index=True, nullable=False)
    info = Column(String, index=True, nullable=False)

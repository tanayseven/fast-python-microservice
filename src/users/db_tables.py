import uuid
from enum import Enum

from sqlalchemy import Column, Text
from sqlalchemy.dialects.postgresql import UUID

from src.database import Base


class UserStatus(Enum):
    CREATED = "created"
    ACTIVATED = "activated"


class User(Base):
    __tablename__ = "user"
    id = Column(UUID, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(Text, nullable=False, unique=True)
    password = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    status = Column(Text, nullable=False, default=lambda: str(UserStatus.CREATED.value))
    verification_id = Column(UUID, nullable=False, default=lambda: str(uuid.uuid4()))

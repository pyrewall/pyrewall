from datetime import datetime
from typing import Any
from uuid import UUID
from uuid_extensions import uuid7

from sqlalchemy import Uuid, String, DateTime, Boolean, ForeignKey, Integer, func, JSON, SmallInteger
from sqlalchemy.orm import mapped_column, Mapped

from .base_model import Base

class AuthSource(Base):
    __tablename__ = 'auth_sources'

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, index=True, unique=True, nullable=False)
    enabled: Mapped[bool] = mapped_column(Boolean, nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    priority: Mapped[int] = mapped_column(SmallInteger, nullable=False)

    type: Mapped[str] = mapped_column(String(50), nullable=False)

    config: Mapped[dict] = mapped_column(JSON, nullable=True)

    created_date: Mapped[datetime] = mapped_column(DateTime, insert_default=func.current_timestamp(), default=None, nullable=False)
    created_by: Mapped[UUID] = mapped_column(ForeignKey('users.id'), nullable=False)

    modified_date: Mapped[datetime] = mapped_column(DateTime, insert_default=func.current_timestamp(), onupdate=func.current_timestamp(), default=None, nullable=False)
    modified_by: Mapped[UUID] = mapped_column(ForeignKey('users.id'), nullable=False)

    def __init__(self, **kw: Any):
        super().__init__(**kw)

        self.id = uuid7()
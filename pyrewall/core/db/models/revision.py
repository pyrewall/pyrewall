from datetime import datetime
from uuid import UUID
from sqlalchemy import Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base

class Revision(Base):
    __tablename__ = 'revisions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, index=True, unique=True, nullable=False)
    previous_revision_id: Mapped[int] = mapped_column(ForeignKey('revisions.id'), nullable=True)
    owner_id: Mapped[UUID] = mapped_column(ForeignKey('users.id'), nullable=False)
    created_date: Mapped[datetime] = mapped_column(DateTime, insert_default=datetime.now(), default=None, nullable=False)
    commit_date: Mapped[datetime] = mapped_column(DateTime, default=None, nullable=True)
    applied_date: Mapped[datetime] = mapped_column(DateTime, default=None, nullable=True)

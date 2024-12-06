from datetime import datetime
from uuid import UUID

from sqlalchemy import ForeignKey, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped

from .base_model import Base

class UserGroup(Base):
    __tablename__ = 'user_groups'

    user_id: Mapped[UUID] = mapped_column(ForeignKey('users.id'), primary_key=True, index=True, nullable=False)
    group_id: Mapped[UUID] = mapped_column(ForeignKey('groups.id'), primary_key=True, index=True, nullable=False)
    
    created_date: Mapped[datetime] = mapped_column(DateTime, insert_default=func.current_timestamp(), default=None, nullable=False)
    created_by: Mapped[UUID] = mapped_column(ForeignKey('users.id'), nullable=False)

    modified_date: Mapped[datetime] = mapped_column(DateTime, insert_default=func.current_timestamp(), onupdate=func.current_timestamp(), default=None, nullable=False)
    modified_by: Mapped[UUID] = mapped_column(ForeignKey('users.id'), nullable=False)
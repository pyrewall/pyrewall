from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from .base_model import Base

class UserGroup(Base):
    __tablename__ = 'user_groups'

    user_id: Mapped[UUID] = mapped_column(ForeignKey('users.id'), primary_key=True, index=True, nullable=False)
    group_id: Mapped[UUID] = mapped_column(ForeignKey('groups.id'), primary_key=True, index=True, nullable=False)
    
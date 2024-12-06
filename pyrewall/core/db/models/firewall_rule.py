from uuid import UUID
from uuid_extensions import uuid7

from sqlalchemy import Uuid, Boolean, Integer, SmallInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base

class FirewallRule(Base):
    __tablename__ = 'firewall_rules'

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, index=True, nullable=False)
    revision_id: Mapped[int] = mapped_column(ForeignKey('revision.id'), primary_key=True, index=True, nullable=False)
    enabled: Mapped[bool] = mapped_column(Boolean, nullable=False)


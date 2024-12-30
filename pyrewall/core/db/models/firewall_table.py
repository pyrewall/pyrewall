from uuid import UUID
from uuid_extensions import uuid7

from sqlalchemy import Uuid, Boolean, Enum, SmallInteger, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from ...enums.firewall_action import FirewallAction
from ..mixins.has_revision import HasRevisionMixin

from .base_model import Base

class FirewallTable(Base, HasRevisionMixin):
    __tablename__ = 'firewall_tables'

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, index=True, nullable=False)
    default_action: Mapped[FirewallAction] = mapped_column(Enum(FirewallAction), nullable=False)

    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    default_log: Mapped[bool] = mapped_column(Boolean, nullable=False)
    

    def __init__(self, **kw):
        super().__init__(**kw)

        self.id = uuid7()
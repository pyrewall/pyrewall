from uuid import UUID
from uuid_extensions import uuid7

from sqlalchemy import Uuid, Boolean, Enum, SmallInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from ...enums.firewall_action import FirewallAction
from ...enums.firewall_state import FirewallState
from ..mixins.base_rule import BaseRuleMixin

from .base_model import Base

class FirewallRule(Base, BaseRuleMixin):
    __tablename__ = 'firewall_rules'

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, index=True, nullable=False)
    firewall_table_id: Mapped[UUID] = mapped_column(ForeignKey('firewall_tables.id'), nullable=False, index=True)
    
    action: Mapped[FirewallAction] = mapped_column(Enum(FirewallAction), nullable=False)
    state: Mapped[int] = mapped_column(SmallInteger, nullable=False)

    def __init__(self, **kw):
        super().__init__(**kw)

        self.id = uuid7()
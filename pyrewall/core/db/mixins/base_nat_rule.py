from psycopg.types.range import NumericRange
from sqlalchemy import Boolean, ForeignKey, Integer, Uuid, String, Enum, ARRAY, Text
from sqlalchemy.dialects.postgresql import INET, CIDR, INT4RANGE, Range
from sqlalchemy.orm import mapped_column, Mapped

from .base_rule import BaseRuleMixin

class BaseNatRuleMixin(BaseRuleMixin):
    translation_address: Mapped[str] = mapped_column(INET, nullable=False)
    translation_port_range: Mapped[Range[int]] = mapped_column(INT4RANGE, nullable=True)
from sqlalchemy import Boolean, ForeignKey, Integer, Uuid, String, Enum, ARRAY, Text
from sqlalchemy.dialects.postgresql import INET, CIDR, INT4RANGE, Range
from sqlalchemy.orm import mapped_column, Mapped

from ...enums.ip_protocol import IpProtocol
from ...enums.ip_version import IpVersion

from .has_revision import HasRevisionMixin

class BaseRuleMixin(HasRevisionMixin):
    order: Mapped[int] = mapped_column(Integer, nullable=False)
    ip_version: Mapped[IpVersion] = mapped_column(Enum(IpVersion), nullable=False)
    ip_protocol: Mapped[IpProtocol] = mapped_column(Enum(IpProtocol), nullable=False)
    
    invert_source_match: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    source_address: Mapped[str] = mapped_column(INET, nullable=True)
    source_port_range: Mapped[Range[int]] = mapped_column(INT4RANGE, nullable=True)

    invert_destination_match: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    destination_address: Mapped[str] = mapped_column(INET, nullable=True)
    destination_port_range: Mapped[Range[int]] = mapped_column(INT4RANGE, nullable=True)

    log: Mapped[bool] = mapped_column(Boolean, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
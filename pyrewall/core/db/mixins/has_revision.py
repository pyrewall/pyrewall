from sqlalchemy import Boolean, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

class HasRevisionMixin():
    revision_id: Mapped[int] = mapped_column(ForeignKey('revision.id'), index=True)
    enabled: Mapped[bool] = mapped_column(Boolean)
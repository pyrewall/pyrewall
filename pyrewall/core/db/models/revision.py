from datetime import datetime
from sqlalchemy import Integer, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base

class Revision(Base):
    __tablename__ = 'revision'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, index=True, unique=True, nullable=False)
    
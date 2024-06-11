from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database import Base


class UserContactInfo(Base):
    __tablename__ = 'UserContactInfo'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('UserProfile.id'), nullable=False)
    product_id: Mapped[list[int]] = mapped_column(ForeignKey('Products.id'), nullable=False, unique=True)
    country: Mapped[str]
    email: Mapped[Optional[str]]
    address: Mapped[str]
    tel_number: Mapped[str]

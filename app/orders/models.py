from dataclasses import dataclass

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from app.infrastructure.database import Base


class Orders(Base):
    __tablename__ = 'Orders'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('UserProfile.id'), nullable=False)
    product_name: Mapped[str] = mapped_column(nullable=True)
    product_quantity: Mapped[str] = mapped_column(nullable=True)
    price: Mapped[int] = mapped_column(nullable=True)
    status: Mapped[str] = mapped_column(nullable=True)
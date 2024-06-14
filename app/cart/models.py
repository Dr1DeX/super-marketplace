from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database import Base


class Cart(Base):
    __tablename__ = 'Cart'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    product_name: Mapped[str]
    quantity: Mapped[int] = mapped_column(nullable=False, default=1)
    price: Mapped[int] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('UserProfile.id'), nullable=False)

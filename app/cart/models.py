from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database import Base


class CartItem(Base):
    __tablename__ = 'Cart'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('UserProfile.id'), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey('Products.id'), nullable=False, unique=True)

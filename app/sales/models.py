from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database import Base


class ProcessedOrders(Base):
    __tablename__ = 'ProcessedOrders'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    order_id: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('UserProfile.id'), nullable=False)
    country: Mapped[str] = mapped_column(nullable=True)
    tel_num: Mapped[str]
    email: Mapped[str] = mapped_column(nullable=True)
    product_name: Mapped[str]
    product_quantity: Mapped[int]
    product_price: Mapped[int]
    status: Mapped[str] = mapped_column(default='Created')
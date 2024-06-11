from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database import Base


class Products(Base):
    __tablename__ = 'Products'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str]
    product_count: Mapped[int]
    category_id: Mapped[int] = mapped_column(ForeignKey('Categories.id'), nullable=False)


class Categories(Base):
    __tablename__ = 'Categories'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str]

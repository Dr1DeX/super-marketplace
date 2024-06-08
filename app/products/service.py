from dataclasses import dataclass

from app.exception import ProductNotFoundException, ProductByCategoryNameException
from app.products.repository import ProductRepository
from app.products.schema import ProductSchema, CategorySchema


@dataclass
class ProductService:
    product_repository: ProductRepository

    async def get_products(self) -> list[ProductSchema]:
        products = await self.product_repository.get_products()
        products_schema = [ProductSchema.model_validate(product) for product in products]
        return products_schema

    async def get_product(self, product_id: int) -> ProductSchema:
        product = await self.product_repository.get_product(product_id=product_id)

        if not product:
            raise ProductNotFoundException

        return ProductSchema.model_validate(product)

    async def get_categories(self) -> list[CategorySchema]:
        categories = await self.product_repository.get_categories()
        categories_schema = [CategorySchema.model_validate(category) for category in categories]
        return categories_schema

    async def get_products_by_category_name(self, category_name: str) -> list[ProductSchema]:
        products = await self.product_repository.get_products_by_categories_name(category_name=category_name)

        if not products:
            raise ProductByCategoryNameException

        products_schema = [ProductSchema.model_validate(product) for product in products]
        return products_schema

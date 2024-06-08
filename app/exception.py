class ProductNotFoundException(Exception):
    detail = 'Product not found'


class ProductByCategoryNameException(Exception):
    detail = 'Product by category name not found'

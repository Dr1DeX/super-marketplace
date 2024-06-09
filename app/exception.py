class ProductNotFoundException(Exception):
    detail = 'Product not found'


class ProductByCategoryNameException(Exception):
    detail = 'Product by category name not found'


class UserNotFoundException(Exception):
    detail = 'User not found'


class UserWrongPasswordException(Exception):
    detail = 'Wrong password'


class TokenExpireExtension(Exception):
    detail = 'Token has expired'


class TokenNotCorrectException(Exception):
    detail = 'Token is not correct'

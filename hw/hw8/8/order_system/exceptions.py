class OrderError():
    pass

class InvalidPriceError(OrderError):
    pass

class InvalidQuantityError(OrderError):
    pass

class InvalidDiscountError(OrderError):
    pass
def apply_discount(price, percent):
    """Она возвращает цену после применения скидки.

    Args:
        price (int): _description_
        percent (int): _description_
    """
    return price - price * percent / 100

if __name__ == "__main__":
    print(apply_discount(2000, 25))

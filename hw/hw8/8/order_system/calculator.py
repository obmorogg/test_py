def calculate_total(price, quantity, discount=0):
    """    Алгоритм:

    1. Посчитать стоимость:

    ```text
    price * quantity
    ```

    2. Вычесть указанный процент скидки.

    Например:

    ```text
    1000 * 3 = 3000
    скидка 10% = 300
    итого = 2700
    ```
    """
    print(f'{price} * {quantity} = {price * quantity}')
    print(f'Скидка {price * quantity * discount / 100} ')
    print(f'Итого {price * quantity - price * quantity * discount / 100}')
    pass
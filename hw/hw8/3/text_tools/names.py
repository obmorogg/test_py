def format_name(name:str):
    """Функция должна убрать пробелы по краям и привести имя к нормальному виду:
    "   иВАН   " → "Иван"
    Args:
        name (str): _description_
    """

    return name.lower().strip().title()

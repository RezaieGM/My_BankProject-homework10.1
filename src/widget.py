from datetime import datetime
from typing import Optional
from .masks import mask_card, mask_account
def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета в строке.
    Аргументы:
        info (str): Строка формата 'Тип Номер'.
    Возвращает:
        str: Замаскированная строка.
    """
    parts = info.split()
    number = parts[-1]
    name = " ".join(parts[:-1])

    if name.lower() == "счет":
        masked = mask_account(number)
    else:
        masked = mask_card(number)

    return f"{name} {masked}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из ISO-формата в 'ДД.ММ.ГГГГ'.
    Аргументы:
        date_str (str): Дата в формате 'YYYY-MM-DDTHH:MM:SS.ssssss'.
    Возвращает:
        str: Дата в формате 'ДД.ММ.ГГГГ'.
    """
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")
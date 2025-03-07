# src/utils.py
from datetime import datetime

from .masks import mask_account, mask_card


def text_reverse(new_string: str) -> str:
    """Переворачивает строку.

    Args:
        new_string: Исходная строка.

    Returns:
        Перевернутая строка.
    """
    return new_string[::-1]


def mask_account_card(info: str) -> str:
    """Маскирует номер карты/счета в строке.

    Args:
        info: Строка формата 'Тип Номер'.

    Returns:
        Маскированная строка.
    """
    parts = info.split()
    number = parts[-1]
    name = " ".join(parts[:-1])
    masked = mask_account(number)\
        if name.lower() == "счет" else mask_card(number)
    return f"{name} {masked}"


def get_date(date_str: str) -> str:
    """Конвертирует дату из ISO в формат DD.MM.YYYY.

    Args:
        date_str: Дата в ISO формате.

    Returns:
        Отформатированная дата.
    """
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")

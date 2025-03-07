# src/masks.py
def mask_card(number: str) -> str:
    """Маскирует номер карты, оставляя первые 6 и последние 4 цифры.

    Args:
        number: Исходный номер карты (16 цифр).

    Returns:
        Маскированный номер карты.
    """
    if len(number) != 16 or not number.isdigit():
        return number
    return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"


def mask_account(number: str) -> str:
    """Маскирует номер счета, оставляя последние 4 цифры.

    Args:
        number: Исходный номер счета.

    Returns:
        Маскированный номер счета.
    """
    if len(number) < 4 or not number.isdigit():
        return number
    return f"**{number[-4:]}"

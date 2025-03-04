def mask_card(number: str) -> str:
    """Маскирует номер карты, оставляя первые 6 и последние 4 цифры."""
    if len(number) != 16 or not number.isdigit():
        return number
    return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"


def mask_account(number: str) -> str:
    """Маскирует номер счета, оставляя последние 4 цифры."""
    if len(number) < 4 or not number.isdigit():
        return number
    return f"**{number[-4:]}"

# Новая пустая строка должна быть здесь (после последней закрывающей кавычки)

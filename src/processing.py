from typing import List, Dict


def filter_by_state(
    operations: List[Dict], state: str = "EXECUTED"
) -> List[Dict]:
    """
    Фильтрует операции по указанному статусу.

    Args:
        operations: Список операций (словари).
        state: Статус для фильтрации (по умолчанию 'EXECUTED').

    Returns:
        Список отфильтрованных операций.
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(operations: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует операции по дате.

    Args:
        operations: Список операций (словари).
        reverse: Флаг обратной сортировки (по умолчанию True).

    Returns:
        Отсортированный список операций.
    """
    return sorted(operations, key=lambda x: x["date"], reverse=reverse)

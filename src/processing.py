import collections
import re
from datetime import datetime


def filter_by_state(
    list_of_operations: list[dict[str, str | int]], state: str = "EXECUTED"
) -> list[dict[str, str | int]]:
    """Функция возвращает новый список словарей, в которых значение state соответствует заданному"""
    sorting_state = []
    for operation in list_of_operations:
        # Безопасный доступ к ключу
        if operation.get("state") == state:
            sorting_state.append(operation)
    return sorting_state


def sort_by_date(
    list_of_operations: list[dict[str, str | int]], sorting_order: bool = True
) -> list[dict[str, str | int]]:
    """Функция сортирует по дате с поддержкой timestamp"""

    def date_to_string(operation: dict[str, str | int]) -> str:
        date_value = operation.get("date", "")

        # Если это timestamp (число)
        if isinstance(date_value, (int, float)) and date_value > 0:
            try:
                # Преобразуем timestamp в строку даты
                dt = datetime.fromtimestamp(date_value)
                return dt.strftime("%Y-%m-%d")
            except Exception:
                return ""

        # Если это строка
        return str(date_value) if date_value else ""

    return sorted(list_of_operations, key=date_to_string, reverse=sorting_order)


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Сортировка банковских операций по описанию"""
    if not search:
        return data
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    filtered_transactions = []
    for transaction in data:
        description = transaction.get("description")

        if pattern.search(str(description)):
            filtered_transactions.append(transaction)

    return filtered_transactions


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция для подсчета количества операций по категориям"""
    if not categories:
        return data
    categories_list = []
    for transaction in data:
        description = transaction.get("description")
        if description in categories:
            categories_list.append(description)
    categories_count = collections.Counter(categories_list)
    return dict(categories_count)

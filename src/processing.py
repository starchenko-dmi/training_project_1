def filter_by_state(
    list_of_operations: list[dict[str, str | int]], state: str = "EXECUTED"
) -> list[dict[str, str | int]]:
    """Функция возвращает новый список словарей, в которых значение state соответствует заданному"""
    sorting_state = []
    for operation in list_of_operations:
        if operation["state"] == state:
            sorting_state.append(operation)
    return sorting_state


def sort_by_date(
    list_of_operations: list[dict[str, str | int]], sorting_order: bool = True
) -> list[dict[str, str | int]]:
    """Функция сортирует по дате и возвращает отсортированный список по умолчанию от последней операции к предыдущим"""
    data = sorted(list_of_operations, key=lambda operation: operation["date"], reverse=sorting_order)
    return data

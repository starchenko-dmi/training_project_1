def filter_by_state(list_of_operations: list[dict], state='EXECUTED') -> list[dict]:
    """Функция возвращает новый список словорей, в которых занчение state соответствует заданному"""
    sorting_state = []
    for operation in list_of_operations:
        if operation['state'] == state:
            sorting_state.append(operation)
    return sorting_state


def sort_by_date(list_of_operations: list[dict], sorting_order=True) -> list[dict]:
    """Функция сортирует по дате и возвращает отсортированный список, по умолчанию от последней операции к предыдущим"""
    data = sorted(list_of_operations, key=lambda operation: operation['date'], reverse=sorting_order)
    return data
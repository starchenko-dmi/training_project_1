def filter_by_state(list_of_operations: list[dict], state='EXECUTED') -> list[dict]:
    """Функция возвращает новый список словорей, в которых занчение state соответствует заданному"""
    sorting_state = []
    for operation in list_of_operations:
        if operation['state'] == state:
            sorting_state.append(operation)
    return sorting_state

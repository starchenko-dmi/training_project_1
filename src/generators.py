from typing import Generator

def filter_by_currency(list_transact: list[dict[str, str | int]], monnaie: str) -> Generator:
    """Генераторная функция, возвращающая транзакции по заданной валюте"""
    transaction_filtr = (
        transact for transact in list_transact if monnaie == transact["operationAmount"]["currency"]["name"]
    )
    yield from transaction_filtr


def transaction_descriptions(list_transact: list[dict[str, str | int]]) -> Generator:
    """Генераторная функция возвращает описание каждой операции по очереди"""
    yield from (transact["description"] for transact in list_transact)


def card_number_generator(beginning: int, end: int) -> Generator:
    """Генерирует номер карты в формате xxxx xxxx xxxx xxxx"""
    for num in range(beginning, end + 1):
        nomber = f"{num:016d}"
        yield f"{nomber[0: 4]} {nomber[4: 8]} {nomber[8: 12]} {nomber[12:]}"

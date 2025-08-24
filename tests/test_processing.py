import pytest

from src.processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date


@pytest.fixture()
def test_state_data() -> list[dict[str, str | int]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_1(test_state_data: list[dict[str, str | int]], state: str = "EXECUTED") -> None:
    """Тест функции filter_by_state"""
    assert filter_by_state(test_state_data, state) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_2(test_state_data: list[dict[str, str | int]], state: str = "CANCELED") -> None:
    """Тест функции filter_by_state"""
    assert filter_by_state(test_state_data, state) == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_sort_by_date(test_state_data: list[dict[str, str | int]]) -> None:
    """Тест функции sort_by_date"""
    assert sort_by_date(test_state_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def sample_transaction():
    """Фикстура с пустым списком"""
    return []


@pytest.fixture
def sample_transactions():
    """Фикстура с тестовыми данными"""
    return [
        {"id": 1, "description": "Покупка в магазине продуктов", "amount": -1250.50, "currency": "RUB"},
        {"id": 2, "description": 'Зарплата от компании ООО "Рога и копыта"', "amount": 50000.00, "currency": "RUB"},
        {"id": 3, "description": "Перевод от Иванова И.И.", "amount": 10000.00, "currency": "RUB"},
    ]


def test_search_by_word(sample_transactions):
    """Тест поиска по слову"""
    result = process_bank_search(sample_transactions, "Магазин")
    assert len(result) == 1
    assert result[0]["description"] == "Покупка в магазине продуктов"


def test_case_insensitive_search(sample_transaction):
    """Тест при пустом списке операций"""
    result = process_bank_search(sample_transaction, "МАГАЗИН")
    assert result == []


def test_empty_transactions_list():
    """Тест с пустым списком транзакций"""
    transactions = []
    categories = ["Продукты", "Рестораны"]

    result = process_bank_operations(transactions, categories)
    expected = {}

    assert result == expected


def test_case_sensitive_search():
    """Тест регистрозависимого поиска"""
    transactions = [{"description": "Продукты"}, {"description": "продукты"}, {"description": "ПРОДУКТЫ"}]
    categories = ["Продукты", "продукты", "ПРОДУКТЫ"]

    result = process_bank_operations(transactions, categories)
    expected = {"Продукты": 1, "продукты": 1, "ПРОДУКТЫ": 1}

    assert result == expected


def test_categories_not_in_transactions():
    """Тест когда категории есть, но их нет в транзакциях"""
    transactions = [{"description": "Продукты"}, {"description": "Рестораны"}]
    categories = ["Продукты", "Рестораны", "Одежда", "Транспорт"]

    result = process_bank_operations(transactions, categories)
    expected = {"Продукты": 1, "Рестораны": 1}

    assert result == expected


def test_duplicate_transactions():
    """Тест с дублирующимися транзакциями"""
    transactions = [{"description": "Продукты"}, {"description": "Продукты"}, {"description": "Продукты"}]
    categories = ["Продукты"]

    result = process_bank_operations(transactions, categories)
    expected = {"Продукты": 3}

    assert result == expected

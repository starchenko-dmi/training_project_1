import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture()
def list_transact() -> list[dict[str, str | int]]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


def test_filter_by_currency_usd(list_transact: list[dict[str, str | int]]) -> None:
    """Тест функции filter_by_currency"""
    result = list(filter_by_currency(list_transact, "USD"))
    assert result == [
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        }
    ]


def test_filter_by_currency_rub(list_transact: list[dict[str, str | int]]) -> None:
    """Тест функции filter_by_currency"""
    result = list(filter_by_currency(list_transact, "RUB"))
    assert result == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]


def test_filter_by_currency_empty() -> None:
    """Тест функции filter_by_currency"""
    result = list(filter_by_currency([], "RUB"))
    assert result == []


def test_transaction_descriptions(list_transact: list[dict[str, str | int]]) -> None:
    """Тест проверки функции transaction_descriptions"""
    result = list(transaction_descriptions(list_transact))
    assert result == ["Перевод организации", "Перевод со счета на счет"]


def test_transaction_descriptions_empty() -> None:
    """Тест проверки функции transaction_descriptions"""
    result = list(transaction_descriptions([]))
    assert result == []


@pytest.mark.parametrize(
    "begin, end_1, expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (
            10,
            15,
            [
                "0000 0000 0000 0010",
                "0000 0000 0000 0011",
                "0000 0000 0000 0012",
                "0000 0000 0000 0013",
                "0000 0000 0000 0014",
                "0000 0000 0000 0015",
            ],
        ),
        (
            1000202045000001,
            1000202045000005,
            [
                "1000 2020 4500 0001",
                "1000 2020 4500 0002",
                "1000 2020 4500 0003",
                "1000 2020 4500 0004",
                "1000 2020 4500 0005",
            ],
        ),
    ],
)
def test_card_number_generator(begin, end_1, expected):
    """Тест для проверки функции card_number_generator"""
    result = list(card_number_generator(begin, end_1))
    assert result == expected

import pytest

import json

from src.utils import receiving_financial_transactions


test_data = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 667307132,
    "state": "EXECUTED",
    "date": "2019-07-13T18:51:29.313309",
    "operationAmount": {
      "amount": "97853.86",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на счет",
    "from": "Maestro 1308795367077170",
    "to": "Счет 96527012349577388612"
  }
]

def test_receiving_financial_transactions() -> None:
    """Tests receiving financial transactions"""
    assert receiving_financial_transactions("test_operations.json") == test_data


def test_receiving_financial_transactions_error_1() -> None:
    """Tests receiving financial transactions error 1"""
    assert receiving_financial_transactions("test_error_1.json") == []

def test_receiving_financial_transactions_error_2() -> None:
    """Tests receiving financial transactions error 1"""
    assert receiving_financial_transactions("test_operations_error.json") == []




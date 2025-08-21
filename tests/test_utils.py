import json
from unittest.mock import mock_open, patch

from src.utils import receiving_financial_transactions


def test_receiving_financial_transactions_success():
    """Тест успешного чтения JSON файла"""
    # Подготовка тестовых данных
    test_data = [
        {"id": 1, "date": "2023-01-01", "amount": 1500.00, "currency": "RUB", "description": "Покупка продуктов"},
        {"id": 2, "date": "2023-01-02", "amount": 5000.00, "currency": "RUB", "description": "Зарплата"},
    ]

    # Преобразуем данные в JSON строку
    json_string = json.dumps(test_data, ensure_ascii=False)

    # Мокируем открытие файла
    with patch("builtins.open", mock_open(read_data=json_string)) as mock_file:
        result = receiving_financial_transactions("data/operations.json")

        # Проверяем, что файл открывался правильно
        mock_file.assert_called_once_with("data/operations.json", "r", encoding="utf-8")

        # Проверяем результат
        assert result == test_data
        assert isinstance(result, list)
        assert len(result) == 2


def test_receiving_financial_transactions_error_1() -> None:
    """Tests receiving financial transactions error 1"""
    assert receiving_financial_transactions("test_error_1.json") == []


def test_receiving_financial_transactions_error_2() -> None:
    """Tests receiving financial transactions error 1"""
    assert receiving_financial_transactions("test_operations_error.json") == []

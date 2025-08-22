import json
from unittest.mock import mock_open, patch

from src.utils import receiving_financial_transactions, get_data_csv, get_data_excel

from unittest.mock import patch

import pandas as pd
import pytest


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


# Тесты для CSV
def test_get_data_csv_success():
    """Тест успешного чтения CSV файла"""
    test_data = pd.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"], "amount": [100.0, 200.0]})

    expected_result = [{"id": 1, "name": "Alice", "amount": 100.0}, {"id": 2, "name": "Bob", "amount": 200.0}]

    with patch("src.utils.pd.read_csv", return_value=test_data):
        result = get_data_csv("fake_path.csv")
        assert result == expected_result


def test_get_data_csv_file_not_found():
    """Тест обработки FileNotFoundError"""
    with patch("src.utils.pd.read_csv", side_effect=FileNotFoundError()):
        result = get_data_csv("nonexistent.csv")
        assert result == []


def test_get_data_csv_empty_file():
    """Тест обработки пустого файла"""
    with patch("src.utils.pd.read_csv", side_effect=pd.errors.EmptyDataError()):
        result = get_data_csv("empty.csv")
        assert result == []


def test_get_data_csv_parser_error():
    """Тест обработки ошибки парсинга"""
    with patch("src.utils.pd.read_csv", side_effect=pd.errors.ParserError()):
        result = get_data_csv("corrupted.csv")
        assert result == []


def test_get_data_csv_unexpected_error():
    """Тест обработки неожиданной ошибки"""
    with patch("src.utils.pd.read_csv", side_effect=Exception("Unexpected error")):
        result = get_data_csv("any_file.csv")
        assert result == []


# Тесты для Excel
def test_get_data_excel_success():
    """Тест успешного чтения Excel файла"""
    test_data = pd.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"], "amount": [100.0, 200.0]})

    expected_result = [{"id": 1, "name": "Alice", "amount": 100.0}, {"id": 2, "name": "Bob", "amount": 200.0}]

    with patch("src.utils.pd.read_excel", return_value=test_data):
        result = get_data_excel("fake_path.xlsx")
        assert result == expected_result


def test_get_data_excel_file_not_found():
    """Тест обработки FileNotFoundError"""
    with patch("src.utils.pd.read_excel", side_effect=FileNotFoundError()):
        result = get_data_excel("nonexistent.xlsx")
        assert result == []


def test_get_data_excel_empty_file():
    """Тест обработки пустого файла"""
    with patch("src.utils.pd.read_excel", side_effect=pd.errors.EmptyDataError()):
        result = get_data_excel("empty.xlsx")
        assert result == []


def test_get_data_excel_parser_error():
    """Тест обработки ошибки парсинга"""
    with patch("src.utils.pd.read_excel", side_effect=pd.errors.ParserError()):
        result = get_data_excel("corrupted.xlsx")
        assert result == []


def test_get_data_excel_unexpected_error():
    """Тест обработки неожиданной ошибки"""
    with patch("src.utils.pd.read_excel", side_effect=Exception("Unexpected error")):
        result = get_data_excel("any_file.xlsx")
        assert result == []

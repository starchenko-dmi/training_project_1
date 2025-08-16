from unittest.mock import patch

import pandas as pd
import pytest

from src.read_utils import get_data_csv, get_data_excel


# Тесты для CSV
def test_get_data_csv_success():
    """Тест успешного чтения CSV файла"""
    test_data = pd.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"], "amount": [100.0, 200.0]})

    expected_result = [{"id": 1, "name": "Alice", "amount": 100.0}, {"id": 2, "name": "Bob", "amount": 200.0}]

    with patch("src.read_utils.pd.read_csv", return_value=test_data):
        result = get_data_csv("fake_path.csv")
        assert result == expected_result


def test_get_data_csv_file_not_found():
    """Тест обработки FileNotFoundError"""
    with patch("src.read_utils.pd.read_csv", side_effect=FileNotFoundError()):
        result = get_data_csv("nonexistent.csv")
        assert result == []


def test_get_data_csv_empty_file():
    """Тест обработки пустого файла"""
    with patch("src.read_utils.pd.read_csv", side_effect=pd.errors.EmptyDataError()):
        result = get_data_csv("empty.csv")
        assert result == []


def test_get_data_csv_parser_error():
    """Тест обработки ошибки парсинга"""
    with patch("src.read_utils.pd.read_csv", side_effect=pd.errors.ParserError()):
        result = get_data_csv("corrupted.csv")
        assert result == []


def test_get_data_csv_unexpected_error():
    """Тест обработки неожиданной ошибки"""
    with patch("src.read_utils.pd.read_csv", side_effect=Exception("Unexpected error")):
        result = get_data_csv("any_file.csv")
        assert result == []


# Тесты для Excel
def test_get_data_excel_success():
    """Тест успешного чтения Excel файла"""
    test_data = pd.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"], "amount": [100.0, 200.0]})

    expected_result = [{"id": 1, "name": "Alice", "amount": 100.0}, {"id": 2, "name": "Bob", "amount": 200.0}]

    with patch("src.read_utils.pd.read_excel", return_value=test_data):
        result = get_data_excel("fake_path.xlsx")
        assert result == expected_result


def test_get_data_excel_file_not_found():
    """Тест обработки FileNotFoundError"""
    with patch("src.read_utils.pd.read_excel", side_effect=FileNotFoundError()):
        result = get_data_excel("nonexistent.xlsx")
        assert result == []


def test_get_data_excel_empty_file():
    """Тест обработки пустого файла"""
    with patch("src.read_utils.pd.read_excel", side_effect=pd.errors.EmptyDataError()):
        result = get_data_excel("empty.xlsx")
        assert result == []


def test_get_data_excel_parser_error():
    """Тест обработки ошибки парсинга"""
    with patch("src.read_utils.pd.read_excel", side_effect=pd.errors.ParserError()):
        result = get_data_excel("corrupted.xlsx")
        assert result == []


def test_get_data_excel_unexpected_error():
    """Тест обработки неожиданной ошибки"""
    with patch("src.read_utils.pd.read_excel", side_effect=Exception("Unexpected error")):
        result = get_data_excel("any_file.xlsx")
        assert result == []

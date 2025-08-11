from unittest.mock import Mock, patch

from src.external_api import transaction_amount


def test_transaction_amount_rub():
    """Тест для транзакции в рублях (без конвертации)"""
    transaction = {
        "date": "2019-07-03T18:35:29.512364", "operationAmount":
            {"amount": 1500.50, "currency": {"code": "RUB"}}
    }

    result = transaction_amount(transaction)
    assert result == 1500.50


@patch("src.external_api.requests.get")
def test_transaction_amount_usd(mock_get):
    """Тест транзакции в доллорах с использованием patch и Mock"""
    mock_response = Mock()
    mock_response.json.return_value = {"success": True, "result": 120000.00}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response
    transaction = {
        "date": "2019-07-03T18:35:29.512364", "operationAmount":
            {"amount": 1500, "currency": {"code": "USD"}}
    }
    result = transaction_amount(transaction)
    assert result == 120000.00
    mock_get.assert_called_once()


@patch("src.external_api.requests.get")
def test_transaction_amount_amount(mock_get):
    """Тест ошибочного значения amount"""
    mock_response = Mock()
    mock_response.json.return_value = {"success": False, "result": 120000.00}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response
    transaction = {
        "date": "2019-07-03T18:35:29.512364", "operationAmount":
            {"amount": 1500, "currency": {"code": "USD"}}
    }
    result = transaction_amount(transaction)
    assert result is None
    mock_get.assert_called_once()


@patch("src.external_api.API_KEY", None)  # Подменяем API_KEY на None
def test_transaction_amount_no_api_key():
    """Тест для случая, когда API ключ отсутствует"""

    # Создаём транзакцию (даже простую, функция всё равно вернёт None из-за отсутствия ключа)
    transaction = {
        "date": "2019-07-03T18:35:29.512364", "operationAmount":
            {"amount": 100, "currency": {"code": "USD"}}
    }

    # Вызываем функцию
    result = transaction_amount(transaction)

    # Проверяем, что вернулся None
    assert result is None


@patch("src.external_api.requests.get")
def test_transaction_amount_value_error(mock_get):
    """Тест для случая, когда API возвращает некорректные данные (ValueError)"""

    # Создаём mock-ответ, который вызовет ValueError
    mock_response = Mock()
    mock_response.json.return_value = {"success": True, "result": "некорректное_значение"}  # Это строка, а не число!
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    # Создаём транзакцию
    transaction = {
        "date": "2019-07-03T18:35:29.512364", "operationAmount":
            {"amount": 100, "currency": {"code": "USD"}}
    }

    # Вызываем функцию
    result = transaction_amount(transaction)

    # Проверяем, что функция вернула None (из-за ValueError)
    assert result is None

    # Проверяем, что запрос был сделан
    mock_get.assert_called_once()

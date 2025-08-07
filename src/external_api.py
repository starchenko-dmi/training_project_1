import os

import requests
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Получаем API ключ из переменных окружения
API_KEY = os.getenv("EXCHANGE_API_KEY")
headers = {"apikey": API_KEY}


def transaction_amount(transaction) -> float:
    """Возвращает сумму транзакции в рублях"""

    # Проверяем, что API ключ доступен
    if not API_KEY:
        print("Ошибка: Не найден API ключ EXCHANGE_API_KEY")
        return None

    currency_code = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]

    # Если уже в рублях - возвращаем как есть
    if currency_code == "RUB":
        return float(amount)
    else:
        # Конвертируем в рубли
        url = "https://api.apilayer.com/exchangerates_data/convert"
        params = {"from": currency_code, "to": "RUB", "amount": amount}

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            result_data = response.json()

            # Проверяем успешность ответа API
            if result_data.get("success"):
                return round(float(result_data["result"]), 2)
            else:
                error_info = result_data.get("error", {})
                print(f"Ошибка API: {error_info.get('info', 'Неизвестная ошибка')}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Ошибка запроса: {e}")
            return None
        except (KeyError, ValueError) as e:
            print(f"Ошибка обработки данных: {e}")
            return None

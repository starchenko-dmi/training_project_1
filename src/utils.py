import json


def receiving_financial_transactions(file_path) -> list:
    """Функция для обработки списка транзакций из json файла"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка: Некорректный JSON в файле {file_path}: {e}")
        return []
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return []

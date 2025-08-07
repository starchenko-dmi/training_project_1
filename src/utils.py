import json

def receiving_financial_transactions(json_file) -> list:
    """Функция для обработки списка транзакций из json файла"""
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Ошибка: Файл {json_file} не найден")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка: Некорректный JSON в файле {json_file}: {e}")
        return []
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return []
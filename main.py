


def file_format():
    """Выбор с каким файлом будем работать"""
    while True:  # Бесконечный цикл
        print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        result = input("Введите номер пункта: ").strip()

        if result == "1":
            print("Для обработки выбран JSON-файл")
            return result
        elif result == "2":
            print("Для обработки выбран CSV-файл")
            return result
        elif result == "3":
            print("Для обработки выбран XLSX-файл")
            return result
        else:
            print(f"Выбрано неверное значение: {result}")
            print("Пожалуйста, попробуйте снова.\n")


def status():
    """Выбор статуса"""
    status_cod = ["EXECUTED", "CANCELED", "PENDING"]
    while True:  # Бесконечный цикл
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

        result = input("Введите статус: ").strip()

        if result.upper() in status_cod:
            return result.upper()
        else:
            print(f"Статус операции '{result}' недоступен.")

def parameters():
    """Выбор параметров"""
    while True:


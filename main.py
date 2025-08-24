from pathlib import Path

from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.utils import get_data_csv, get_data_excel, receiving_financial_transactions
from src.widget import get_date, mask_account_card

file_format_selection = []


def file_format() -> list[dict[str, str | int]]:
    """Выбор с каким файлом будем работать"""
    while True:  # Бесконечный цикл
        print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        result = input("Введите номер пункта: ").strip()
        file_format_selection.append(result)

        if result == "1":
            print("Для обработки выбран JSON-файл")
            script_dir = Path(__file__).parent
            json_path = script_dir / "data" / "operations.json"
            list_operations = receiving_financial_transactions(str(json_path))
            return list_operations

        elif result == "2":
            print("Для обработки выбран CSV-файл")
            script_dir = Path(__file__).parent
            csv_path = script_dir / "data" / "transactions.csv"
            list_operations = get_data_csv(str(csv_path))
            return list_operations
        elif result == "3":
            print("Для обработки выбран XLSX-файл")
            script_dir = Path(__file__).parent
            excel_path = script_dir / "data" / "transactions_excel.xlsx"
            list_operations = get_data_excel(str(excel_path))
            return list_operations
        else:
            print(f"Выбрано неверное значение: {result}")
            print("Пожалуйста, попробуйте снова.\n")


def status() -> str:
    """Выбор статуса"""
    status_cods = ["EXECUTED", "CANCELED", "PENDING"]
    while True:  # Бесконечный цикл
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

        result = input("Введите статус: ").strip()

        if result.upper() in status_cods:
            return result.upper()
        else:
            print(f"Статус операции '{result}' недоступен.")


def main():
    """Главная функция"""
    list_operations = file_format()
    status_cod = status()
    list_operations_state = filter_by_state(list_operations, state=status_cod)
    list_operations_data = []
    list_operations_currency = []
    list_operations_search = []
    lict_result = []

    # Сортировка по дате
    while True:

        sort_date = input("Отсортировать операции по дате? Да/Нет: ")
        if sort_date.strip().lower() == "да":
            sort_direction = input("Отсортировать по возрастанию/по убыванию? ")
            if sort_direction.strip().lower() == "по убыванию":
                list_operations_data = sort_by_date(list_operations)
                break
            elif sort_direction.strip().lower() == "по возрастанию":
                list_operations_data = sort_by_date(list_operations, sorting_order=False)
                break
            else:
                print("Введено не верное значение")
        elif sort_date.strip().lower() == "нет":
            list_operations_data = list_operations_state
            break

    # Сортировка по валюте
    while True:
        sort_currency = input("Выводить только рублевые транзакции? Да/Нет: ")
        user_input = sort_currency.strip().lower()

        if user_input == "да":
            if file_format_selection == ["1"]:
                list_operations_currency = [
                    op
                    for op in list_operations_data
                    if op.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
                ]
            elif file_format_selection == ["2"] or file_format_selection == ["3"]:
                list_operations_currency = [op for op in list_operations_data if op.get("currency_code") == "RUB"]
            break

        elif user_input == "нет":
            list_operations_currency = list_operations_data
            break

        else:
            print(f"Выбрано неверное значение: {sort_currency}")
            print("Пожалуйста, попробуйте снова.\n")

    # Сортировка по описанию
    while True:
        sort_search = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ")
        if sort_search.strip().lower() == "да":
            search = input("Введите слово для поиска: ")
            list_operations_search = process_bank_search(list_operations_currency, search)
            break
        elif sort_search.strip().lower() == "нет":
            list_operations_search = list_operations_currency
            break
        else:
            print(f"Выбрано неверное значение: {sort_search}")
            print("Пожалуйста, попробуйте снова.\n")

    print("Распечатываю итоговый список транзакций...")
    if len(list_operations_search) > 0:
        print(f"Всего банковских операций в выборке: {len(list_operations_search)}")
        print()
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    # Печать результатов
    if file_format_selection == ["1"]:
        for op in list_operations_search:
            if op.get("from") is None:
                operation = (
                    f"{get_date(op.get('date'))} {op.get('description')}\n"
                    f"{mask_account_card(op.get('to'))}\n"
                    f"Сумма: {op.get('operationAmount', {}).get('amount')} "
                    f"{op.get('operationAmount', {}).get('currency', {}).get('name')}"
                )
                lict_result.append(operation)

            else:
                operation = (
                    f"{get_date(op.get('date'))} {op.get('description')}\n"
                    f"{mask_account_card(op.get('from'))} -> {mask_account_card(op.get('to'))}\n"
                    f"Сумма: {op.get('operationAmount', {}).get('amount')} "
                    f"{op.get('operationAmount', {}).get('currency', {}).get('name')}"
                )
                lict_result.append(operation)

    elif file_format_selection == ["2"] or file_format_selection == ["3"]:
        for op in list_operations_search:
            value = op.get("from")
            value_1 = op.get("to")

            if value != value:
                operation = (
                    f"{get_date(op.get('date'))} {op.get('description')}\n"
                    f"{mask_account_card(str(op.get('to')))}\n"
                    f"Сумма: {op.get('amount')} {op.get('currency_code')}"
                )
                lict_result.append(operation)
            elif value != value and value_1 != value_1:
                pass

            else:
                operation = (
                    f"{get_date(op.get('date'))} {op.get('description')}\n"
                    f"{mask_account_card(op.get('from'))} -> {mask_account_card(op.get('to'))}\n"
                    f"Сумма: {op.get('amount')} {op.get('currency_code')}"
                )
                lict_result.append(operation)

    for operation in lict_result:
        print(operation)
        print()  # Пустая строка между операциями


if __name__ == "__main__":
    main()

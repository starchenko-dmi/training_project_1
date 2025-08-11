import json
import logging
import os

# Создаем папку logs, если её нет
os.makedirs("logs", exist_ok=True)

# Настраиваем логирование
logging.basicConfig(
    filename='logs/utils.log',  # Файл будет в папке logs с расширением .log
    filemode='w',                      # 'w' означает перезапись файла при каждом запуске
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Формат: время - имя модуля - уровень - сообщение
    level=logging.INFO,                # Уровень логирования (можно изменить при необходимости)
    encoding='utf-8'                   # Кодировка файла (рекомендуется указывать)
)

# Создаем логгер
logger = logging.getLogger(__name__)


def receiving_financial_transactions(file_path) -> list:
    """Функция для обработки списка транзакций из json файла"""
    logger.info("Функция receiving_financial_transactions запущена")
    try:
        logger.info("Чтение данных из json файла")
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            logger.info("Работа функции receiving_financial_transactions завершилась успехом")
            return data
    except FileNotFoundError:
        logger.exception(f"Ошибка: Файл {file_path} не найден")
        return []
    except json.JSONDecodeError as e:
        logger.exception(f"Ошибка: Некорректный JSON в файле {file_path}: {e}")
        return []
    except Exception as e:
        logger.exception(f"Неожиданная ошибка: {e}")
        return []

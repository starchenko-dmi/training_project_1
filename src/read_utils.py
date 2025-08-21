import logging
import os

import pandas as pd

# Создаем папку logs, если её нет
os.makedirs("logs", exist_ok=True)


# Настраиваем логирование
logging.basicConfig(
    filename="logs/read_utils.log",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    encoding="utf-8",
)

# Создаем логгер
logger = logging.getLogger(__name__)


def get_data_csv(file_path: str) -> list:
    """Получение данных из CSV файла"""
    logger.info("Функция get_data_csv запущена")
    try:
        logger.info("Чтение данных из csv файла")
        df = pd.read_csv(file_path)
        data = df.to_dict(orient="records")
        logger.info(f"Успешно прочитано {len(data)} записей")
        return data
    except FileNotFoundError:
        logger.error(f"Ошибка: Файл {file_path} не найден")
        return []
    except pd.errors.EmptyDataError:
        logger.error(f"Ошибка: Файл {file_path} пустой")
        return []
    except pd.errors.ParserError as e:
        logger.error(f"Ошибка парсинга CSV файла {file_path}: {e}")
        return []
    except Exception as e:
        logger.error(f"Неожиданная ошибка при чтении {file_path}: {e}")
        return []


def get_data_excel(file_path: str) -> list:
    """Получение данных из Excel файла"""
    logger.info("Функция get_data_excel запущена")
    try:
        logger.info("Чтение данных из excel файла")
        df = pd.read_excel(file_path)
        data = df.to_dict(orient="records")
        logger.info(f"Успешно прочитано {len(data)} записей")
        return data
    except FileNotFoundError:
        logger.error(f"Ошибка: Файл {file_path} не найден")
        return []
    except pd.errors.EmptyDataError:
        logger.error(f"Ошибка: Файл {file_path} пустой")
        return []
    except pd.errors.ParserError as e:
        logger.error(f"Ошибка парсинга excel файла {file_path}: {e}")
        return []
    except Exception as e:
        logger.error(f"Неожиданная ошибка при чтении {file_path}: {e}")
        return []

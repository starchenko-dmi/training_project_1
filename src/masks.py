import logging
import os

# Создаем папку logs, если её нет
os.makedirs("logs", exist_ok=True)

# Настраиваем логирование
logging.basicConfig(
    filename='logs/masks.log',  # Файл будет в папке logs с расширением .log
    filemode='w',                      # 'w' означает перезапись файла при каждом запуске
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Формат: время - имя модуля - уровень - сообщение
    level=logging.INFO,                # Уровень логирования (можно изменить при необходимости)
    encoding='utf-8'                   # Кодировка файла (рекомендуется указывать)
)

# Создаем логгер
logger = logging.getLogger(__name__)


def get_mask_card_number(card_number: int) -> str:
    """Возвращает маску номера карты"""
    logger.info(f"Функция get_mask_card_number запущена")
    if len(str(card_number)) == 16:
        logger.info(f"Функция get_mask_card_number успешно отработала")
        return f"{str(card_number)[0:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"
    else:
        logger.error("Произошла ошибка: Не верный номер карты!")
        raise ValueError("Не верный номер карты")


def get_mask_account(account: int) -> str:
    """Возвращает маску номера счета"""
    logger.info(f"Функция get_mask_account запущена")
    if len(str(account)) == 20:
        logger.info(f"Функция get_mask_account успешно отработала")
        return f"**{str(account)[-4:]}"
    else:
        logger.error("Произошла ошибка: Не верный номер счета!")
        raise ValueError("Не верный номер счета")

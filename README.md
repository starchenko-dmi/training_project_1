# Учебный проект работы банковского терминала

Проект содержит 4 деректории:
1. masks.py Содержит 2 функции:
    1. get_mask_card_number - Маскирование номера карты
    2. get_mask_account - Маскирование номера счета
2. processing.py содержит 2 функции:
    1. filter_by_state - Сортировки банковских операций по параметру state (по умолчанию "EXECUTED")
    2. sort_by_date - Сортировки банковских операций по дате (по умолчанию от последних операций к предыдущим)
3. widget.py содержит 2 функции:
    1. mask_account_card - Извлекает и строкового значения номер карты или счета и возвращает маску
    2. get_date - Декодирует дату и возврашает её в вормате ДД.ММ.ГГГГ
4. generators.py содержит 3 генераторных функции:
    1. filter_by_currency - Генераторная функция, возвращающая транзакции по заданной валюте
    2. transaction_descriptions - Генераторная функция возвращает описание каждой операции по очереди
    3. card_number_generator - Генерирует номер карты в формате xxxx xxxx xxxx xxxx по заданным значения начала и конца генерации

Написаны тесты на модуль masks.py, processing.py, widget.py и generators.py тестами покрыто 100 процентов кода, отчет имеется.

## Установка и использование. 
Как его устанавливать и использовать я пока сам не знаю, но предоставляю насткойки и зависимости проекта:
[tool.poetry]
name = "training-project-1"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.13"


[tool.poetry.group.lint.dependencies]
flake8 = "^7.3.0"
mypy = "^1.16.1"
black = "^25.1.0"
isort = "^6.0.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.mypy]
disallow_untyped_defs = true
no_implicit_optional = true
check_untyped_defs = true
strict = true
warn_unreachable = true
warn_return_any = true
exclude = 'venv'

[tool.black]
Максимальная длина строки
line-length = 119
Файлы, которые не нужно форматировать
exclude = ".git"

[tool.isort]
максимальная длина строки
line_length = 119

# Учебный проект работы банковского терминала

Проект содержит 4 функции:
1. Маскирование номера карты
2. Маскирование номера счета
3. Сортировки банковских операций по параметру state (по умолчанию "EXECUTED")
4. Сортировки банковских операций по дате (по умолчанию от последних операций к предыдущим)

Написанны тесты на модуль masks.py и processing.py

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
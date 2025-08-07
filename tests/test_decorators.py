import pytest

from src.decorators import log


@log()
def division(x, y):
    result = x / y
    return result


def test_log(capsys):
    division(6, 2)
    # Перехватываем вывод
    captured = capsys.readouterr()
    assert captured.out == "division Ok\n"


def test_log_error(capsys):
    # Ожидаем, что функция бросит ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        division(6, 0)

    # Проверяем вывод ПОСЛЕ завершения функции
    captured = capsys.readouterr()
    assert captured.out == "division error: division by zero. Inputs: ((6, 0), {})\n"

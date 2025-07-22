import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture()
def test_card_number() -> int:
    return 2202202197240155


@pytest.fixture()
def test_account() -> int:
    return 40817810944057830862


def test_mask_card_number(test_card_number: int) -> None:
    """Тестирует функцию get_mask_card_number"""
    assert get_mask_card_number(test_card_number) == "2202 20** **** 0155"


def test_mask_account(test_account: int) -> None:
    """Тестирует функцию get_mask_account"""
    assert get_mask_account(test_account) == "**0862"


def test_mask_card_number_invalid_min() -> None:
    """Тест функции get_mask_card_number с недостающим количеством символов"""
    with pytest.raises(ValueError):
        get_mask_card_number(220220219742015)


def test_mask_card_number_invalid_max() -> None:
    """Тест функции get_mask_card_number с избыточным количеством символов"""
    with pytest.raises(ValueError):
        get_mask_card_number(22022021974201555)


def test_get_mask_account_invalid_min() -> None:
    """Тест функции get_mask_account с недостающим количеством символов"""
    with pytest.raises(ValueError):
        get_mask_account(4081781094405783086)


def test_get_mask_account_invalid_max() -> None:
    """Тест функции get_mask_account с избыточным количеством символов"""
    with pytest.raises(ValueError):
        get_mask_account(408178109440578308622)

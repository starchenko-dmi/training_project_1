import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.fixture()
def test_card_number():
    return 2202202197240155

@pytest.fixture()
def test_account():
    return 40817810944057830862


def test_mask_card_number(test_card_number):
    """Тестирует функцию get_mask_card_number"""
    assert get_mask_card_number(test_card_number) == '2202 20** **** 0155'


def test_mask_account(test_account):
    """Тестирует функцию get_mask_account"""
    assert get_mask_account(test_account) == '**0862'


def test_mask_card_number_invalid_min():
    with pytest.raises(ValueError):
        get_mask_card_number(220220219742015)


def test_mask_card_number_invalid_max():
    with pytest.raises(ValueError):
        get_mask_card_number(22022021974201555)


def test_get_mask_account_invalid_min():
    with pytest.raises(ValueError):
        get_mask_account(4081781094405783086)


def test_get_mask_account_invalid_max():
    with pytest.raises(ValueError):
        get_mask_account(408178109440578308622)
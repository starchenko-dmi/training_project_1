import pytest

from src.widget import get_date, mask_account_card


@pytest.fixture()
def test_data() -> str:
    return "2024-03-11T02:26:18.671407"


@pytest.mark.parametrize(
    "data_card, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(data_card: str, expected: str) -> None:
    """Тест функции mask_account_card"""
    assert mask_account_card(data_card) == expected


def test_get_date(test_data: str) -> None:
    """Тест функции get_date"""
    assert get_date(test_data) == "11.03.2024"


def test_get_date_invalid() -> None:
    """Тест функции get_mask_account с избыточным количеством символов"""
    with pytest.raises(TypeError):
        get_date(" ")

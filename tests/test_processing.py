import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture()
def test_state() -> list[dict[str, str | int]]:
    return


@pytest.fixture()
def test_date() -> list[dict[str, str | int]]:
    return


def test_filter_by_state(test_state: list[dict[str, str | int]]) -> None:
    """Тест функции filter_by_state"""
    assert filter_by_state(test_state) == []


def test_sort_by_date(test_date: list[dict[str, str | int]]) -> None:
    """Тест функции sort_by_date"""
    assert sort_by_date(test_date) == []

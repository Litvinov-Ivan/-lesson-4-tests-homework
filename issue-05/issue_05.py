from what_is_year_now import what_is_year_now
from unittest.mock import patch
import pytest


def test_year_format_1():
    with patch('what_is_year_now.json.load') as mocked_case:
        mocked_case.return_value = {'currentDateTime': '2022-03-01'}
        assert what_is_year_now() == 2022
        mocked_case.assert_called_once()


def test_year_format_2():
    with patch('what_is_year_now.json.load') as mocked_case:
        mocked_case.return_value = {'currentDateTime': '01.03.2019'}
        assert what_is_year_now() == 2019
        mocked_case.assert_called_once()


def test_year_exception():
    with patch('what_is_year_now.json.load') as mocked_case:
        mocked_case.return_value = {'currentDateTime': '01-2022-01'}
        with pytest.raises(ValueError):
            what_is_year_now()
            mocked_case.assert_called_once()


if __name__ == "__main__":
    pytest.main()

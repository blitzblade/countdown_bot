import pytest
from datetime import datetime, date

from functions import calculate_days_left, calculate_target_date, clean_data, count_down

today = date(2023, 1, 1)


def test_calculate_days_left():
    days_left = calculate_days_left(
        end_date="2023-01-05", today=today)

    assert days_left == 4


def test_calculate_target_date():
    target_date = calculate_target_date(4, today=today)

    assert target_date == "2023-01-05"


def test_clean_data_exception():
    data = {
        "days_left": None,
        "target_date": None,
        "action": "leaves Twitter",
        "tweep": "@kwesi_dadson"
    }

    with pytest.raises(RuntimeError):
        clean_data(data)


def test_clean_data_no_days():
    data = {
        "days_left": None,
        "target_date": "2023-01-05",
        "action": "leaves Twitter",
        "tweep": "@kwesi_dadson"
    }

    clean_d = clean_data(data, today=today)

    assert clean_d["days_left"] == 4


def test_clean_data_no_target_date():
    data = {
        "days_left": 4,
        "target_date": "",
        "action": "leaves Twitter",
        "tweep": "@kwesi_dadson"
    }

    clean_d = clean_data(data, today=today)

    assert clean_d["target_date"] == "2023-01-05"


def test_count_down():
    data = {
        "days_left": None,
        "target_date": "2023-01-04",
        "action": "leaves Twitter",
        "tweep": "@kwesi_dadson"
    }
    d, m = count_down(data, today=date(2022, 12, 27))

    assert d["days_left"] == 7
    assert m == "8 days more till @kwesi_dadson leaves Twitter"


def test_count_down_timeup():
    data = {
        "days_left": None,
        "target_date": "2023-01-01",
        "action": "leaves Twitter",
        "tweep": "@kwesi_dadson"
    }
    d, m = count_down(data, today=today)

    assert m == "@kwesi_dadson leaves Twitter today!"


def test_count_down_late():
    data = {
        "days_left": None,
        "target_date": "2022-12-30",
        "action": "leaves Twitter",
        "tweep": "@kwesi_dadson"
    }
    d, m = count_down(data, today=today)

    assert m == None


def test_count_down_1_day():
    data = {
        "days_left": 1,
        "target_date": None,
        "action": "leaves Twitter",
        "tweep": "@kwesi_dadson"
    }
    d, m = count_down(data, today=today)

    assert m == "1 day more till @kwesi_dadson leaves Twitter"

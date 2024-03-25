from os import path
import datetime as dt
import json
import pytest
from widget.widget_table.get_data import get_data, get_last_id, get_last_operations

test_json_path = path.join('tests', 'test_data', 'test.json')


@pytest.fixture
def test_json():
    with open(test_json_path) as tj:
        test_json = json.load(tj)
    return test_json


class TestGetData:
    def test_get_data(self, test_json):
        assert isinstance(get_data(test_json_path), type(test_json))

    def test_get_last_id(self, test_json):
        get_data = test_json  # get_data используется во вложенной функции
        assert len(get_last_id()) == 5
        for sempl in get_last_id():
            for id, date in sempl.items():
                assert isinstance(id, int)
                assert isinstance(date, dt.datetime)

    def test_get_last_operations(self):
        get_data = test_json  # get_data используется во вложенной функции
        assert len(get_last_operations()) == 5
        assert isinstance(get_last_operations(), list)
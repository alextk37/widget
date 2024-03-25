import pytest
from widget.widget_table.transactions import Transaction


@pytest.fixture
def get_unit():
    unit = Transaction(594226727,
                       "CANCELED",
                       "2018-09-12T21:27:25.241689",
                       {"amount": "67314.70",
                        "currency": {"name": "руб.",
                                     "code": "RUB"
                                     }
                        },
                       "Перевод организации",
                       "Visa Platinum 1246377376343588",
                       "Счет 14211924144426031657"
                       )
    return unit


class TestTransaction:

    def test_get_date(self, get_unit):
        unit = get_unit
        unit_none = Transaction()
        assert isinstance(unit.get_date(), str)
        assert len(unit.get_date()) == 10
        assert unit_none.get_date() is None

    def test_is_executed(self, get_unit):
        unit = get_unit
        unit_none = Transaction()
        assert isinstance(unit.is_executed(), str)
        assert unit.is_executed() == 'Отмена'
        assert unit_none.is_executed() is None
        unit.state = 'EXECUTED'
        assert unit.is_executed() == 'Выполнена'

    def test_get_amount(self, get_unit):
        unit = get_unit
        assert isinstance(unit.get_amount(), str)

    def test_get_description(self, get_unit):
        unit = get_unit
        assert isinstance(unit.get_description(), str)

    def test_get_hide_from(self, get_unit):
        unit = get_unit
        unit_none = Transaction()
        assert unit_none.get_hide_from() == 'Нет информации'
        assert unit.get_hide_from() == 'Visa Platinum  1246 37** **** 3588'
        unit.from_ = '84163357546688983493'
        assert unit.get_hide_from() == ' **3493'
        unit.description = 'Открытие вклада'
        assert unit.get_hide_from() == 'Открытие вклада'

    def test_get_hide_to(self, get_unit):
        unit = get_unit
        unit_none = Transaction()
        assert unit_none.get_hide_to() == 'Нет информации'
        assert unit.get_hide_to() == 'Счет  **1657'
        unit.to = 'Visa Platinum 1246377376343588'
        assert unit.get_hide_to() == 'Visa Platinum  1246 37** **** 3588'

    def test_repr(self, get_unit):
        unit = get_unit
        assert unit.__repr__() == 'Transaction id: 594226727'

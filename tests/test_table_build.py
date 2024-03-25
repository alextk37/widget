import pytest
from widget.widget_table.transactions import Transaction
from widget.widget_table.table_build import table_build


@pytest.fixture
def get_unit():
    unit_list = []
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
    for i in range(5):
        unit_list.append(unit)
    return unit_list


def test_table_build(get_unit):
    get_last_operations = get_unit # get_last_operation используется во вложенной функции
    assert table_build() is None

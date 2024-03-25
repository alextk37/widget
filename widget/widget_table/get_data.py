from os import path
import json
from datetime import datetime as dt
from widget.widget_table.transactions import Transaction

DATA_PATH = path.join(path.dirname(path.abspath(__file__)),
                      'operations_data',
                      'operations.json')


def get_data(path) -> json:
    with open(path) as data:
        json_data = json.load(data)
    return json_data


def get_last_id():
    '''
    Возвращает список пяти последних выполненных
    операций с их идентификаторами.

    '''
    operations = []
    dt_format = '%Y-%m-%dT%H:%M:%S.%f'
    for trans in get_data(DATA_PATH):
        if trans.get('state') == 'EXECUTED':
            if trans['date']:
                operations.append(
                    {trans['id']: dt.strptime(trans['date'], dt_format)}
                                )
    operations.sort(key=lambda trans_time: list(trans_time.values())[0],
                    reverse=True)
    return operations[:5]


def get_last_operations():
    '''
    Возвращает список последних операций в виде объектов класса Transaction.

    '''
    operations = get_data(DATA_PATH)
    last_operations = []
    last_id = get_last_id()

    for id in last_id:
        for operation in operations:
            if list(id.keys())[0] == operation.get('id'):
                operation['from_'] = operation.get('from')
                if 'from' in operation.keys():
                    del operation['from']
                last_operations.append(Transaction(**operation))
                break
    return last_operations

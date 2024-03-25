from datetime import datetime as dt


class Transaction:
    '''
    Представляет транзакцию.

    Аргументы:
        id (int): Идентификатор транзакции.
        state (str): Состояние транзакции.
        date (str): Дата транзакции в формате '%Y-%m-%dT%H:%M:%S.%f'.
        operationAmount (float): Сумма транзакции.
        description (str): Описание транзакции.
        from_ (str): Отправитель транзакции.
        to (str): Получатель транзакции.

    Методы:
        __repr__(): Возвращает строковое представление транзакции.
        get_date(): Возвращает отформатированную дату транзакции.
        is_executed(): Возвращает выполнена ли транзакция или отменена.
        get_amount(): Возвращает отформатированную сумму транзакции.
        get_description(): Возвращает описание транзакции.
        get_hide_from(): Возвращает скрытого отправителя транзакции.
        get_hide_to(): Возвращает скрытого получателя транзакции.
    '''
    def __init__(self,
                 id=None,
                 state=None,
                 date=None,
                 operationAmount=None,
                 description=None,
                 from_=None,
                 to=None,) -> None:
        self.id = id
        self.state = state
        self.date = date
        self.operationAmount = operationAmount
        self.description = description
        self.from_ = from_
        self.to = to

    def __repr__(self) -> str:
        return f'Transaction id: {self.id}'

    def get_date(self) -> str:
        if self.date:
            dt_format_in = '%Y-%m-%dT%H:%M:%S.%f'
            dt_format_out = '%d.%m.%Y'
            date_obj = dt.strptime(self.date, dt_format_in)
            return dt.strftime(date_obj, dt_format_out)

    def is_executed(self) -> str:
        if self.state == 'EXECUTED':
            return 'Выполнена'
        elif self.state == 'CANCELED':
            return 'Отмена'

    def get_amount(self) -> str:
        amount_info = self.operationAmount
        return f'{amount_info['amount']} {amount_info['currency']['name']}'

    def get_description(self) -> str:
        return self.description

    def get_hide_from(self) -> str:
        if self.description == 'Открытие вклада':
            return self.description
        if self.from_:
            ac = self.from_
            if ac[-20:].isdigit():
                return f'{ac[:-20]} **{ac[-4:]}'
            return f'{ac[:-16]} {ac[-16:-12]} {ac[-12:-10]}** **** {ac[-4:]}'
        return 'Нет информации'

    def get_hide_to(self) -> str:
        if self.to:
            ac = self.to
            if ac[-20:].isdigit():
                return f'{ac[:-20]} **{ac[-4:]}'
            return f'{ac[:-16]} {ac[-16:-12]} {ac[-12:-10]}** **** {ac[-4:]}'
        return 'Нет информации'

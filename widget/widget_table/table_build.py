from rich.console import Console
from rich.table import Table
from widget.widget_table.get_data import get_last_operations


def table_build() -> Console:
    '''
    Строит таблицу с историей операций по счету.

    Возвращает Объект консоли с построенной таблицей.
    '''

    table_data = get_last_operations()

    table = Table(title='История операций по счету:')

    table.add_column('Дата', justify='right', style='cyan', no_wrap=True)
    table.add_column('Описание', style='magenta')
    table.add_column('Сумма', justify='center', style='green')
    table.add_column('Отправитель', justify='right', style='red')
    table.add_column('Получатель', justify='right', style='red')
    table.add_column('Статус', justify='center', style='green')

    for row in table_data:
        table.add_row(row.get_date(),
                      row.get_description(),
                      row.get_amount(),
                      row.get_hide_from(),
                      row.get_hide_to(),
                      row.is_executed()
                      )

    console = Console()
    return console.print(table)

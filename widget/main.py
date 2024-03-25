import time
from rich import print
from rich.progress import Progress
from widget_table.table_build import table_build


def main() -> None:
    print(":receipt:", "[bold red]История операций по счету:[/bold red]")
    with Progress() as progress:
        message = '[bold red]Загружаю информацию...'
        upload_data = progress.add_task(message, total=50)
        while not progress.finished:
            progress.update(upload_data, advance=0.5)
            time.sleep(0.01)
    table_build()


if __name__ == '__main__':
    main()

from pathlib import Path
from lab5.order_processor import OrderProcessor


def main():
    try:
        orders_file = Path(__file__).parent / "orders.txt"
        processor = OrderProcessor(orders_file)
        processor.process()

    except FileNotFoundError:
        print("Ошибка: файл orders.txt не найден.")

    except PermissionError:
        print("Ошибка: недостаточно прав для работы с файлом.")


if __name__ == "__main__":
    main()

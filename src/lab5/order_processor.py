from lab5.order import Order

class OrderProcessor:

    def __init__(self, input_file):
        self.__input_file = input_file
        self.__orders = []
        self.__errors = []

    def read_orders(self):
        with open(self.__input_file, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.rstrip("\r\n")

                if not line:
                    continue

                parts = line.split(";")

                if len(parts) != 6:
                    print(
                        f"Строка {line_number} пропущена: "
                        "неверное количество полей"
                    )
                    continue

                order = Order(*parts)
                errors = order.get_errors()

                if errors:
                    self.__errors.extend(errors)
                else:
                    self.__orders.append(order)

    def sort_orders(self):
        self.__orders.sort(
            key=lambda order: order.get_sort_key()
        )

    def save_orders(self):
        with open(
            "order_country.txt", "w", encoding="utf-8"
        ) as file:
            for order in self.__orders:
                file.write(order.format_order() + "\n")

    def save_errors(self):
        with open(
            "non_valid_orders.txt", "w", encoding="utf-8"
        ) as file:
            for error in self.__errors:
                file.write(error + "\n")

    def process(self):
        self.read_orders()
        self.sort_orders()
        self.save_orders()
        self.save_errors()

        print("Обработка завершена!")
        print(f"Корректных заказов: {len(self.__orders)}")
        print(f"Количество ошибок: {len(self.__errors)}")

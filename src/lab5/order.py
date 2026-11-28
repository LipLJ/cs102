import re
from collections import Counter


class Order:
    PRIORITIES = {
        "MAX": 0,
        "MIDDLE": 1,
        "LOW": 2
    }

    def __init__(self, order_id, products, name, address, phone, priority):
        self.__order_id = order_id
        self.__products = products
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__priority = priority

    def validate_address(self):
        parts = [part.strip() for part in self.__address.split(".")]
        return len(parts) == 4 and all(parts)

    def validate_phone(self):
        pattern = r"\+[0-9]-[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}"
        return bool(re.fullmatch(pattern, self.__phone))

    def get_errors(self):
        errors = []

        if not self.validate_phone():
            value = self.__phone if self.__phone else "no data"
            errors.append(f"{self.__order_id};2;{value}")

        if not self.validate_address():
            value = self.__address if self.__address else "no data"
            errors.append(f"{self.__order_id};1;{value}")

        return errors

    def get_country(self):
        return self.__address.split(".")[0].strip()

    def get_priority(self):
        return self.PRIORITIES[self.__priority]

    def format_products(self):
        products = Counter(
            product.strip()
            for product in self.__products.split(",")
        )

        result = []

        for product, count in products.items():
            if count > 1:
                result.append(f"{product} x{count}")
            else:
                result.append(product)

        return ", ".join(result)

    def format_order(self):
        _, region, city, street = [
            part.strip() for part in self.__address.split(".")
        ]

        return (
            f"{self.__order_id};{self.format_products()};"
            f"{self.__name};{region}. {city}. {street};"
            f"{self.__phone};{self.__priority}"
        )

    def get_sort_key(self):
        country = self.get_country()

        if country == "Россия":
            country = "Российская Федерация"

        return (
            0 if country == "Российская Федерация" else 1,
            country.casefold(),
            self.get_priority()
        )

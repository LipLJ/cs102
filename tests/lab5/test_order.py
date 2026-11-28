from lab5.order import Order
def create_order(address, phone, products="Молоко, Хлеб, Молоко"):
    return Order(
        "12345",
        products,
        "Иванов Иван Иванович",
        address,
        phone,
        "MAX"
    )


def test_valid_address():
    order = create_order(
        "Россия. Москва. Москва. Пушкина",
        "+7-912-345-67-89"
    )
    assert order.validate_address() is True


def test_empty_address():
    order = create_order("", "+7-912-345-67-89")
    assert order.validate_address() is False


def test_invalid_address():
    order = create_order(
        "Япония. Шибуя. Шибуя-кроссинг",
        "+8-131-234-56-78"
    )
    assert order.validate_address() is False


def test_valid_phone():
    order = create_order(
        "Россия. Москва. Москва. Пушкина",
        "+7-912-345-67-89"
    )
    assert order.validate_phone() is True


def test_invalid_phone():
    order = create_order(
        "Германия. Бавария. Мюнхен. Мариенплац",
        "+4-989-234-56"
    )
    assert order.validate_phone() is False


def test_empty_phone():
    order = create_order(
        "Россия. Москва. Москва. Пушкина",
        ""
    )
    assert order.validate_phone() is False


def test_multiple_errors():
    order = create_order("", "")
    assert order.get_errors() == [
        "12345;2;no data",
        "12345;1;no data"
    ]


def test_repeated_products():
    order = create_order(
        "Россия. Москва. Москва. Пушкина",
        "+7-912-345-67-89"
    )
    assert order.format_products() == "Молоко x2, Хлеб"


def test_product_without_repetitions():
    order = create_order(
        "Россия. Москва. Москва. Пушкина",
        "+7-912-345-67-89",
        "Бананы, Гречка, Сметана"
    )
    assert order.format_products() == "Бананы, Гречка, Сметана"


def test_priority():
    assert Order.PRIORITIES["MAX"] == 0
    assert Order.PRIORITIES["MIDDLE"] == 1
    assert Order.PRIORITIES["LOW"] == 2

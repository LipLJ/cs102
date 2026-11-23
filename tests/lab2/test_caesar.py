from src.lab2.caesar import encrypt_caesar, decrypt_caesar


def test_zero_shift():
    assert encrypt_caesar("Hello", 0) == "Hello"


def test_shift_by_one():
    assert encrypt_caesar("ABCxyz", 1) == "BCDyza"


def test_alphabet_wraparound():
    assert encrypt_caesar("XYZ", 3) == "ABC"


def test_decrypt_with_shift():
    assert decrypt_caesar("DEF", 3) == "ABC"


def test_preserve_digits_spaces_and_punctuation():
    assert encrypt_caesar("Hi, Bob! 123", 3) == "Kl, Ere! 123"


def test_empty_string():
    assert encrypt_caesar("", 3) == ""


def test_shift_by_26():
    assert encrypt_caesar("Python", 26) == "Python"


def test_shift_greater_than_26():
    assert encrypt_caesar("ABC", 29) == "DEF"


def test_negative_shift():
    assert encrypt_caesar("ABC", -1) == "ZAB"


def test_lowercase_letters():
    assert encrypt_caesar("xyz", 3) == "abc"


def test_decrypt_lowercase():
    assert decrypt_caesar("abc", 3) == "xyz"


def test_decrypt_preserves_symbols():
    assert decrypt_caesar("Kl, Ere! 123", 3) == "Hi, Bob! 123"


def test_encrypt_then_decrypt():
    text = "Hello, Python 3.14!"
    assert decrypt_caesar(encrypt_caesar(text), 3) == text


def test_spaces_remain_unchanged():
    assert encrypt_caesar("A B C", 1) == "B C D"


def test_punctuation_remains_unchanged():
    assert encrypt_caesar("!@#$%", 3) == "!@#$%"


def test_shift_by_52():
    assert encrypt_caesar("ABC", 52) == "ABC"


def test_negative_shift_round_trip():
    text = "Abc XYZ"
    assert decrypt_caesar(encrypt_caesar(text, -5), -5) == text
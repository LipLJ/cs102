from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere


def test_keyword_a():
    assert encrypt_vigenere("PYTHON", "A") == "PYTHON"


def test_encrypt_example():
    assert encrypt_vigenere("ATTACKATDAWN", "LEMON") == "LXFOPVEFRNHR"


def test_decrypt_example():
    assert decrypt_vigenere("LXFOPVEFRNHR", "LEMON") == "ATTACKATDAWN"


def test_lowercase():
    assert encrypt_vigenere("python", "a") == "python"


def test_preserve_case():
    assert encrypt_vigenere("AttackAtDawn", "LEMON") == "LxfopvEfRnhr"


def test_preserve_spaces_and_punctuation():
    assert encrypt_vigenere("ATTACK AT DAWN!", "LEMON") == "LXFOPV EF RNHR!"


def test_empty_string():
    assert encrypt_vigenere("", "LEMON") == ""


def test_single_letter():
    assert encrypt_vigenere("A", "B") == "B"


def test_wraparound():
    assert encrypt_vigenere("XYZ", "BCD") == "YAC"


def test_decrypt_lowercase():
    assert decrypt_vigenere("lxfopvefrnhr", "LEMON") == "attackatdawn"


def test_encrypt_then_decrypt():
    text = "Hello, Python 3.14!"
    keyword = "LEMON"
    encrypted = encrypt_vigenere(text, keyword)
    assert decrypt_vigenere(encrypted, keyword) == text


def test_keyword_repeats():
    assert encrypt_vigenere("AAAAAA", "BC") == "BCBCBC"

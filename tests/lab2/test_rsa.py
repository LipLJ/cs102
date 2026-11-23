
from src.lab2.rsa import (is_prime, gcd, multiplicative_inverse, generate_keypair, encrypt, decrypt)


def test_is_prime():
    assert is_prime(2)
    assert is_prime(11)
    assert not is_prime(8)
    assert not is_prime(1)
    assert not is_prime(0)
    assert not is_prime(-5)


def test_gcd():
    assert gcd(12, 15) == 3
    assert gcd(3, 7) == 1
    assert gcd(20, 8) == 4
    assert gcd(0, 5) == 5


def test_multiplicative_inverse():
    assert multiplicative_inverse(7, 40) == 23
    assert (7 * multiplicative_inverse(7, 40)) % 40 == 1


def test_multiplicative_inverse_without_solution():
    try:
        multiplicative_inverse(6, 40)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"


def test_generate_keypair():
    public, private = generate_keypair(17, 19)

    assert public[1] == 323
    assert private[1] == 323
    assert (public[0] * private[0]) % (16 * 18) == 1


def test_generate_keypair_rejects_non_prime():
    try:
        generate_keypair(8, 19)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"


def test_generate_keypair_rejects_equal_primes():
    try:
        generate_keypair(17, 17)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"


def test_encrypt_decrypt():
    public, private = generate_keypair(17, 19)
    message = "HELLO"

    encrypted = encrypt(public, message)
    decrypted = decrypt(private, encrypted)

    assert decrypted == message


def test_encrypt_returns_list():
    public, _ = generate_keypair(17, 19)

    encrypted = encrypt(public, "ABC")

    assert isinstance(encrypted, list)
    assert len(encrypted) == 3


def test_empty_message():
    public, private = generate_keypair(17, 19)

    encrypted = encrypt(public, "")
    decrypted = decrypt(private, encrypted)

    assert encrypted == []
    assert decrypted == ""


def test_longer_message():
    public, private = generate_keypair(61, 53)
    message = "Hello, RSA!"

    encrypted = encrypt(public, message)
    decrypted = decrypt(private, encrypted)

    assert decrypted == message

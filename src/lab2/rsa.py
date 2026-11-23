
import random
import typing as tp


def is_prime(n: int) -> bool:
    """
    Tests to see if a number is prime.

    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def gcd(a: int, b: int) -> int:
    """
    Euclid's algorithm for determining the greatest common divisor.

    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    while b != 0:
        a, b = b, a % b

    return abs(a)


def multiplicative_inverse(e: int, phi: int) -> int:
    """
    Euclid's extended algorithm for finding the multiplicative
    inverse of two numbers.

    >>> multiplicative_inverse(7, 40)
    23
    """
    old_r, r = phi, e
    old_s, s = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s

    if old_r != 1:
        raise ValueError("The inverse does not exist.")

    return old_s % phi


def generate_keypair(
    p: int, q: int
) -> tp.Tuple[tp.Tuple[int, int], tp.Tuple[int, int]]:
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal")

    # Calculate n
    n = p * q

    # Calculate phi
    phi = (p - 1) * (q - 1)

    # Choose e such that e and phi are coprime
    e = random.randrange(2, phi)

    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # Calculate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private keys
    return ((e, n), (d, n))


def encrypt(pk: tp.Tuple[int, int], plaintext: str) -> tp.List[int]:
    # Unpack the key
    key, n = pk

    # Encrypt each character
    cipher = [pow(ord(char), key, n) for char in plaintext]

    return cipher


def decrypt(pk: tp.Tuple[int, int], ciphertext: tp.List[int]) -> str:
    # Unpack the key
    key, n = pk

    # Decrypt each character
    plain = [chr(pow(char, key, n)) for char in ciphertext]

    return "".join(plain)


if __name__ == "__main__":
    print("RSA Encrypter/Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number: "))

    public, private = generate_keypair(p, q)

    print("Public key:", public)
    print("Private key:", private)

    message = input("Enter a message to encrypt: ")
    encrypted_msg = encrypt(public, message)

    print("Encrypted message:", encrypted_msg)
    print("Decrypted message:", decrypt(private, encrypted_msg))

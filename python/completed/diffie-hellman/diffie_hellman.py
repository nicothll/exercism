import random


def private_key(p: int) -> int:
    """Function that choose randomly a private key greater than 1 and less than p

    :param p: int - given prime number
    :return: int - private key
    """
    return random.randint(2, p - 1)


def public_key(p: int, g: int, private: int) -> int:
    """Function calculates a Diffie-Hellman public key

    :param p: int - given prime number
    :param g: int - given prime number
    :param private: int - given private key
    :return: int - public key
    """
    return g**private % p


def secret(p: int, public: int, private: int) -> int:
    """Function calculate Diffie-Hellman secret key

    :param p: int - given prime number
    :param public: int - given public key
    :param private: int - given private key
    :return: int - secret key
    """
    return public**private % p

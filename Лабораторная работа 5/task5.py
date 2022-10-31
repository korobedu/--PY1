import string
import random


def get_random_password(n: int = 8) -> str:
    # TODO написать функцию генерации случайных паролей
    passlist = random.sample(string.ascii_lowercase +
                             string.ascii_uppercase +
                             string.digits, n)
    password = "".join(passlist)
    return password


print(get_random_password())

import string
import random

class User:
    def __init__(self, name) -> None:
        self.name = name

def random_string():
    chars = string.ascii_lowercase
    return ''.join(
        [random.choise(chars) for in range(8)]
    )

if __name__ == '__main__':

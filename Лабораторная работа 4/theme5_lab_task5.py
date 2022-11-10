import random
import string


def get_random_password():
    pwd_length = 8


# набор данных (заглавные и строчные буквы, цифры)
    UPPERCASE_CHARACTERS = string.ascii_uppercase
    LOWERCASE_CHARACTERS = string.ascii_lowercase
    DIGITS = string.digits

# весь набор
    combined_list = UPPERCASE_CHARACTERS + LOWERCASE_CHARACTERS + DIGITS

# случайный элемент из каждого набора
    rand_upper = random.choice(UPPERCASE_CHARACTERS)
    rand_lower = random.choice(LOWERCASE_CHARACTERS)
    rand_digit = random.choice(DIGITS)

    temp_pwd = random.sample(combined_list, pwd_length)
    password = "".join(temp_pwd)

    return password

print(get_random_password())

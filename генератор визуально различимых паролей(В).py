from random import sample, shuffle, choice
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits


def generate_password(m):
    valid_symbols = list(set(ascii_letters + digits) - {'0', '1', 'I', 'l', 'o', 'O'})
    valid_lowercase = list(set(ascii_lowercase) - {'I', 'O'})
    valid_uppercase = list(set(ascii_uppercase) - {'I', 'O'})
    valid_digits = list(set(digits) - {'1', '0'})
    symbs = choice(valid_uppercase) + choice(valid_lowercase) + choice(valid_digits)
    valid_symbols2 = list(set(valid_symbols) - set(symbs))
    string = symbs
    string += ''.join(sample(valid_symbols2, m))
    shuffle(list(string))
    return string


def main(n, m):
    passwords = []
    for _ in range(n):
        passwords.append(generate_password(m))
        while passwords[-1] in passwords[:-1]:
            passwords[-1] = generate_password(m)
    return passwords


print(*main(6, 10), sep="\n")

import random as rd
import secrets
import string


def password_gen(pass_length):
    pass_source = string.ascii_letters + string.digits + string.punctuation
    password = secrets.choice(string.ascii_lowercase)
    password += secrets.choice(string.ascii_uppercase)
    password += secrets.choice(string.digits)
    password += secrets.choice(string.punctuation)


    for i in range(0, pass_length-4):
        password += secrets.choice(pass_source)

    pass_list = list(password)
    secrets.SystemRandom().choice(pass_list)
    password = ''.join(pass_list)
    return password



length = int(input('How long would you like your password to be:'))
# digit = int(input('Enter the number of digits you would like:'))
# alph = input('Enter the number of alphabet:')

pas = password_gen(length)
print(pas)

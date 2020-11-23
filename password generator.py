import random as rd
import secrets
import string

num = int(input('How many numbers would you like in your password:'))
alp = int(input('How many alphabets would you like:'))
sm = int(input('How many symbols would you like:'))
choice = int(input('How many choices would you like:'))
pswd =[]

print('The suitable choices for your passwords are:\n')
for i in range(choice):
    x = ''
    y = ''
    z = ''
    u = ''
    for j in range(num):
        x = x + secrets.choice(string.ascii_lowercase)

    for k in range(alp):
        y = y + secrets.choice(string.digits)

    for m in range(sm):
        z = z + secrets.choice(string.punctuation)

    password = x + y + z
    pass_list = list(password)
    rd.shuffle(pass_list)
    password = ''.join(pass_list)
    pswd.append(password)


for j in pswd:
    print(j)





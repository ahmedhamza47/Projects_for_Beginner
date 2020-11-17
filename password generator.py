import random as rd
a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','w','x','y','z']
n = ['0','1','2','3','4','5','6','7','8','9']
sym = ['!','@','$','%','^','&','*','(',')','<','/','-',',','+']

num = int(input('How many numbers would you like in your password:'))
alp = int(input('How many alphabets would you like:'))
sm = int(input('How many symbols would you like:'))
choice =int(input('How many choices would you like:'))
pswd =[]
x = ''
y = ''
z = ''
print('The suitable choices for your passwords are:\n')
for i in range(choice):
    x = ''
    y = ''
    z = ''
    u = ''
    for l in range(num):
       x = x + rd.choice(n)

    for j in range(alp):
        y = y + rd.choice(a)

    for k in range(sm):
        z = z + rd.choice(sym)

    u = x + y + z
    pswd.append(u)


for i in pswd:
    j = rd.shuffle(i)
    print(j)



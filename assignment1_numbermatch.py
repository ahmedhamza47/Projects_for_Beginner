import random as rd
numbers = [1,2,3,4,5,6,7,8,9,10]
selection = ''

for i in range(3):
    com = rd.choice(numbers)
    selection = selection + str(com)

com_select = selection
print(com_select)

user_inp = int(input('Guess the 3 digit number:'))
user_input = str(user_inp)
for i in range(3):
    for  j in range(3):
        if(user_input[i]==com_select[j]):
            print('match')

        elif user_input == com_select:
            print('100% match')
            break
    break

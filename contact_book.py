contact_name = []
contact_number = []


def enter_contact():
    name = input('Enter your contact name:')
    num = input('Enter your contact number:')
    contact_name.append(name)
    contact_number.append(num)

def delete_contact():
    id = int(input('Which contact would you like to delete:'))
    id = id-1
    contact_name.pop(id)
    contact_number.pop(id)

def show_contact():
    print('SN \t Contact Name \t Contact Number')
    j = 0
    k = -1
    x = 0
    for i in contact_name:
        k = k + 1
        for j in range(len(contact_number)):
            x = x+1
            print('%d)'%x,'\t',i, '\t \t \t', contact_number[j + k])
            break

print('Welcome to your contact book:')

print('What would you like to do:\n Press 1) to add contact \n Press 2) to show your contacts\n Press 3) to delete contacts'
    '\n Press 4) to exit')
try:
    while(True):
        enter = int(input('\nEnter Choice:'))
        if(enter == 1):
            enter_contact()
            print('contact added')
        elif(enter == 2):
            if contact_name ==[] and contact_number==[]:
                print('Contact book empty: Please add some contacts to show')
            else:
                show_contact()
        elif(enter == 3):
            if contact_name ==[] and contact_number==[]:
                print('Contact book empty: Please add some contacts to delete')
            else:
                delete_contact()
                print('contact deleted')
        elif(enter == 4):
            break
        else:
            print('Error: please enter numbers between 1-4')
except:
    print('invalid entry')


print('"Thanks  for using contact book" Rerun the program to start again')







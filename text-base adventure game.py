print('Welcome to the text adventure game:')
name = input('Enter your name:')
age = int(input('Enter your age:'))

health = 10
try:
    if age >=18:
        print('Your are old enough to play')
        des = input('Do you want to play?(y/n):').lower()
        if des == 'y':
            print('You are starting with 10 health \n Lets play:')
            choice1 = input('First choice (LEFT OR RIGHT)?').lower()
            if choice1=='left':
                choice2=input('You went left and found a river.Go(above/below)?').lower()
                if choice2 == 'above':
                    print('Great you came across the river safe.')

                else:
                    print('You managed to get to the shore but were wounded by sharks.')
                    health = health-5
                    print('You lost',health,'health')
                choice3 = input('Now you found a bike and a car on the road.Which one should you ride?(bike/car)').lower()
                if choice3 == 'bike':
                    health = health - 2
                    print('You managed to reach the forest but It started raining,you became wet and lost',health,'health')


                elif choice3 =='car':
                    print('You safely managed to reach the forest')

                print('You were walking down the forest till nightfall.You are thirsty and hungry \n You saw a goat.You '
                      'found a knife and a gun but you are confuse what to use.')
                choice4 = input('Knife or Gun?:').lower()
                if choice4=='knife':
                    print('You successfully killed the goat and ate it.')
                else:
                    print('You killed it with a gun but it made a loud noise and drew attention of nearby predators.You were killed')
                    print('you lost')
                    exit()
                print('You came across the forest finally. You won with',health,' health remaining')




            else:
                print('you fell down and died.')

        else:
            pass





    else:
        print('you are too young to play this game')
except SyntaxError:
    print('syntax error. Please restart the game')

print('rerun the program if you want to play again.Thankyou')
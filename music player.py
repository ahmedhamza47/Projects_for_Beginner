from playsound import playsound
my_file = open('F:/Users/hp/Desktop/music/name.txt', 'r')
song_names = my_file.read()
print('Welcome to your music player.')
print('The available songs are:')
print(song_names)
my_file.close()
print('')
while(True):

    name = input('Which song would you like to play:')
    print('music playing')
    playsound('F:/Users/hp/Desktop/music/%s' % name)
    print('music stopped')



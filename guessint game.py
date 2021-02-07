
from random import shuffle
#Initial list
mylist = ['','O','']

def shuffle_list(mylist):
    shuffle(mylist)
    
    return mylist

def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        #recall input() returns a string
        guess= input("Pick a number: 0,1,or 2 ")

    return int(guess)

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Correct Guess!')
    else:
        print('Wrong! Better luck next time')
        print(mylist)

#Initial list
mylist = ['','O','']
#shuffle list
mixedup_list = shuffle_list(mylist)
#user guess
guess = player_guess()
#check guess
check_guess(mixedup_list,guess)
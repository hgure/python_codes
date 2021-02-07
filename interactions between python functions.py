#Interactions between Python Functions
example = [1,2,3,4,5,6,7]
#import shuffle function from random module
from random import shuffle
#shuffle(example)
#print(example)

#create own function that returns a result
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result = shuffle_list(example)
print(result)

mylist = ['','O','']
shuffle_list(mylist)
print(mylist)

def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess= input("Pick a number: 0,1,or 2")

    return int(guess)

player_guess()
myindex = player_guess()
print(myindex)
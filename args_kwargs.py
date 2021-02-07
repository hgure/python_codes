#args - arguments
#kwargs - key word arguments

#def myfunc(a,b,c=0,d=0,e=0):
    #returns 5% of the sum of a and b
#    return sum((a,b,c,d,e))* 0.05

#print(myfunc(40,60))

#kwargs can be any word. as long as it starts with *
#def myfunc(*args):
 #   for item in args:
  #      print(item)


#print(myfunc(40,10,10,10,10,10))

#**kwargs returns a dictionary
#def myfunc(**kwargs):
 #   if 'fruit' in kwargs:
  #      print('My fruit of choice is {}'.format(kwargs['fruit']))
  #  else:
   #     print('I did not find any fruit here')

#myfunc(fruit'apple',)

def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[1],kwargs['food']))

myfunc(10,20,30,fruit='orange', food='eggs',animal='dog')

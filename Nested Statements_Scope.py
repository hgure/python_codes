#x = 25

#def printer():
 #   x = 50
  #  return x

#print(x)

#print(printer())


#x = 50

#def func():
 #   global x
  #  print(f'X is {x}')
    
    #LOCAL REASSIGNMENT ON A GLOBAL VARIABLE
   # x = 'NEW VALUE'
    #print(f'I JUST LOCALLY CHANGED GLOBAL X TO {x}')

#print(x)

#func()
#print(x)


x = 50

def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

func(x)
print('x is still', x)
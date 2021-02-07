def splicer(mystring):
    if len(mystring)%2==0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy', 'Bob', 'Sue']

print(list(map(splicer,names)))
##############
def check_even(num):
    return  num%2==0

numbers=[1.2,3,4,5,6]

print(list(filter(check_even,numbers)))
###############
#Lambda Function

names = ['Andy', 'Bob', 'Sue']
print(list(map(lambda x:x[0],names)))
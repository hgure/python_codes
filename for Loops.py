#print all numbers in list
list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list1:
    print(num)
#print only the even numbers from that list!
for num in list1:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')

#Another common idea during a for loop is keeping some sort of 
# running tally during multiple loops. For example, let's create a for loop that sums up the list:
list_sum = 0 

for num in list1:
    list_sum = list_sum + num

print(list_sum)

#strings are a sequence so when we iterate through them we will be accessing each item in that string.
mystring='Hello World'
for letter in mystring:
    print(letter)

#strings iteration example 2
for letter in 'Hello World':
    print(letter)

#look at how a for loop can be used with a tuple:
tup = (1,2,3,4,5)

for t in tup:
    print(t)

#If you are iterating through a sequence that contains tuples, the item can actually be the tuple itself, this is an example of tuple unpacking
list2 = [(2,4),(6,8),(10,12)]
for tup in list2:
    print(tup)

# Now with tuple unpacking! This prints the first entry in the tuple
for (t1,t2) in list2:
    print(t1)

#more tuple unpacking
list3 = [(1,2,3),(5,6,7),(8,9,10)]

for a,b,c in list3:
    print(b)

#iterate through dictionary
d = {'k1':1,'k2':2,'k3':3}
for key,value in d.items():
    print(value)
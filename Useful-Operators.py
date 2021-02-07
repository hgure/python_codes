#range and generator functions

index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}' .format(index_count,letter))
    index_count+=1

#another example
index_count=0
word='abcde'
for letter in word:
    print(word[index_count])
    index_count+=1

#another example using enumerate function
word='abcde'
for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

#example with zip function
#if lists are different size it uses the smallest set
mylist1=[1,2,3]
mylist2=['a','b','c']
mylist3=[100,200,300]

for item in zip(mylist1,mylist2,mylist3):
    print(item)

list(zip(mylist1,mylist2))

#list comprehension- simplifying for loop into one line
#using list comprehension
celsius = [0,10,20,34.5]

fahrenheit=[((9/5)*temp + 32) for temp in celsius]

print(fahrenheit)
#using for loop
fahrenheit=[]

for temp in celsius:
    fahrenheit.append((9/5)*temp + 32)
print(fahrenheit)


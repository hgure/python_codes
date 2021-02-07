x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x += 1
else:
    print("X IS NOT LESS THAN 5")
#keywords
#break: breaks out of the current closest enclosing loop
#continue: goes to the top of the closest enclosing loop
#pass: does nothing at all 

#using coninue to skip a letter
mystring = 'Sammy'

for letter in mystring:
    if letter == 'a':
        continue
    print(letter)

#using break to skip a letter
mystring = 'Sammy'

for letter in mystring:
    if letter == 'a':
        break
    print(letter)

#more break examples
x = 0

while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
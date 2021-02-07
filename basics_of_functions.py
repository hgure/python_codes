def add_num(num1,num2):
    return num1+num2

result = add_num(10,20)


#different between return and print in a function
#the print does not return an output but return does

def print_result(a,b):
    print(a+b)

def return_result(a,b):
    return a+b
#does not have a return
#return1 = print_result(10,20)
#has a return
return2 = return_result(10,20)
#what is the type
#print(type(return1))
#what is the type
print(type(return2))
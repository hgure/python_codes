#Examples to display logic with functions
#using function to do a even number check
#def even_check(number):
#    return number % 2 == 0
    

#print(even_check(20))
#print(even_check(15))

#Return true if any number is even inside a list
#def check_even_list(num_list):
#    for number in num_list:
#        if number % 2 == 0:
#            return True
#        else:
#            pass

#check_even_list([1,1,1])
#return all the even numbers in a list
def check_even_list(num_list):
    
    #placeholder variables
    even_numbers = []
    
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers

print(check_even_list([1,4,5,6]))


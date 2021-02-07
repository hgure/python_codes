def user_choice():
    #Two conditions to check
    #Digit or within_range == false
    choice ='WRONG'
    acceptable_range = range(0,10)
    within_range = False
    
    while choice.isdigit() == False or within_range == False:
        
    
    
        choice = input("Please enter a number (0-10): ")
        #Digit Check
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")
        #Range Check
        if choice.isdigit() == True:
            if int(choice) in range(0,10):
                within_range = True
                print(" That number is a digit and within range")
            else:
                print("Sorry you are out of acceptable range (0-10)")
                within_range = False
                
                
        
    
    return int(choice)

user_choice()
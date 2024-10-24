"""
Exercise 6: Brute Force Attack
"""
password = 12345    #Defining the correct password.
while password == 12345: #Using a while loop to repeatedly ask the user for the password until the correct one is entered.
    password_typed = int(input("Enter the password: ")) #asking user to enter the password
    if password_typed==12345:
        print("The password is correct.")   #prints if the user enters the correct password.
        break   # Exits the loop if the password is correct.
    else:
        print("The password is incorrect. Try again!")   #prints if the user enters the wrong password
        
"""
Optional Requirements:
"""
password = 12345
maximum_attempts = 5  #maximum number of attempts.
#using a while loop to repeatedly ask the user for the password but with attempts this time.
while maximum_attempts>0:
    password_typed = int(input("Enter the password: "))
    if password_typed==password:
        print("The password is correct.")
        break
    else:
        maximum_attempts= maximum_attempts-1  # Decrements the number of attempts.
        if maximum_attempts>0:
            print(f"Incorrect, you have {maximum_attempts} attempts left.")# Notifies the user of remaining attempts.
        else:
            # Notifies the user of maximum attempts reached.
            print("Maximum number of attempts reached, Security has been notified.")
            break
if maximum_attempts ==0:  # Checking if attempts have ran out.
    print("Your access is denied, kindly contact the customer service.") #an appropriate message for the output.
     

    
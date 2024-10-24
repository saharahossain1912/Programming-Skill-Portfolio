"""
Exercise 10: Is it even?
"""
def eve_odd(num):   # Function determining if the number is even or odd.
    if (num % 2)==0:  #Checking if the number is even.
        return f"The number {num} is even." # Returning a message indicating the number is even.
    else:
        return f"The number {num} is odd." # Returning a message indicating the number is odd.
        
def main():    #asking the user for a number from within the main function.
    user_input = int(input("Enter a number: "))
    
    output = eve_odd(user_input) #Sending the entered number to the eve_odd function.
    print(output)    #printing the message returned by the function.
    
if __name__ == "__main__":  #calling main fuction.
    main()


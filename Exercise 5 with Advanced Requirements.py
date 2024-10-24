"""
Exercise 5: Days of the Month 
"""
#Creating a dictionary where the keys are month numbers and the values are the number of days in those months.
month= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 
        10: 31, 11: 30, 12: 31}
#Asking the user to input the month number.
num= int(input("Enter the month number: "))
#printing the number of days after checking if the input is valid.
if (num>=1 and num<=12):
    print(f"The number of days in month {num} is {month[num]}") # Prints the no.of days in the month entered.
else:
    print("Input is invalid. Kindly enter a number between 1 and 12.") # Prints an error message if the entered month number is not valid.
    
"""
Advanced Requirement:
"""
    
def year(leap_year):  #checking the leap year.
    return(leap_year % 4 == 0 and leap_year % 100 != 0) or (leap_year % 400 == 0)
#Creating a dictionary called 'month'.
month= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 
            10: 31, 11: 30, 12: 31}
#Asking the user to input the month number.
num= int(input("Enter the month number: "))
#Asking if it is a leap year If user picks the month of February.
if num==2:
   leap_year=int(input("Enter the year: ")) #asking user to enter the year
   if year(leap_year):
       print("February in a leap year has 29 days.")  #prints if user enters a leap year
   else:
        print("February has 28 days.")  #prints if user enters a non-leap year.
elif (num>=1 and num<=12):              #prints if user enters other month apart from february.
    print(f"The number of days in month {num} is {month[num]}")
else:
    print("Input is invalid. Kindly enter a number between 1 and 12.")

    
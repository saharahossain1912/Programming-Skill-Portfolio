"""
Exercise 4: Primitive Quiz
"""
capital = input("What is the capital of France? ")   #Asking the user a question.
if capital == "Paris":
    print("The answer is correct.")  #prints if user enters the correct password.
else:
    print("The answer is wrong.")    #prints if user enters the wrong password.
    
"""
Advanced Requirements
"""
capital = input("What is the capital of France? ")  
if capital.lower() == "paris": #Checking if the input, converted to lowercase, matches "paris"
    print("The answer is correct.")
else:
    print("The answer is wrong.")
    
"""
Multiple Questions: Extend the program into a quiz that asks for
the capitals of 10 European countries. Provide feedback for each question.
"""
print("Primitive Quiz")
# Defining a dictionary with European countries as keys and their capitals as values.
European_countries = {'Germany': 'Berlin',
                      'Switzerland': 'Bern',
                      'Spain': 'Madrid',
                      'Italy': 'Rome',
                      'Portugal': 'Lisbon',
                      'Netherlands': 'Amsterdam',
                      'Belgium': 'Brussels',
                      'Austria': 'Vienna',
                      'Poland': 'Warsaw',
                      'Greece': 'Athens'}
#Creating a function 'check' to check the user's answer.
def check(country,cap):
    user_input = input(f"What is the capital of {country}? ") #Asking the user for the capital of the given country.
    if user_input == cap.lower(): #Comparing the user's answer with the correct capital
        print(f"The capital of {country} is {cap}.")
    else:
        print(f"The capital of {country} is not {cap}.")
#Looping through each country and its capital from the dictionary.
for country, cap in European_countries.items():
    check(country, cap)   #Calling the check function.


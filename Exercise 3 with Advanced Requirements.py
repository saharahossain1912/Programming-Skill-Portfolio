"""
Exercise 3: Biography
"""
#Storing the information as key-value pairs in a dictionary 'saharas_dict'.
saharas_dict = {'Name': "Sahara",
                'Hometown': "Chittagong",
                'Age': 19}
#Printing the values on separate lines using a single print() statement.
print(saharas_dict['Name'])  
print(saharas_dict['Hometown'])
print(saharas_dict['Age'])  

"""
Advanced Requirements
"""
Name= input("Enter your name: ")  #Taking user input for name, hometown, and age.
Hometown = input("Enter your hometown: ")
Age = int(input("Enter your age: "))
# Storing user input in the dictionary 'saharas_dict'.
saharas_dict = {'Name': Name,     
                'Hometown': Hometown,
                'Age': Age}
#Printing the values on separate lines.
print(saharas_dict['Name'])  
print(saharas_dict['Hometown'])
print(saharas_dict['Age'])  

"""
Try giving both your first and second name when asked for your name.
What happens? How can you handle multiple words in Python?

Answer: Multiple words can be naturally handled by Python's input() method. 
Therefore, "Sahara Hossain" will be correctly stored as a single string value
if you enter it as the name.
"""

"""
Test the program by entering a string value for age (e.g., "twenty"). 
What happens? How can you prevent this issue?

If I enter nineteen as my age, it will show error because the above age
input has int() function as it's data type so here python will only accept 
an integer but if we remove the int() function, python will accept
both string and integer.
"""
Age= input("Enter your age: ") #both 19 and nineteen are accepted.












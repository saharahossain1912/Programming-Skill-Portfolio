"""
Exercise 8: Simple Search
"""
# Initializing the list with specific names.
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
print(names[-2])  #prints Sam from the list.

"""
Optional Requirements:
1) Allow the user to input the search term instead of using a predefined value.
"""
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
entered_name = input("Enter the name: ")  #Allowing the user to input the name.
if entered_name in names:    #To check if the search term is in the list
    print(f"{entered_name} is in the list.")  #prints if the entered name is in the list.
else:
    print(f"{entered_name} is not in the list.")   #prints if the entered name is not in the list.
    
"""
2) Implement the search functionality based on user input.
"""
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
entered_name = input("Enter the name: ")
def search_name(names, entered_name): #Function to search for the term in the list
    if entered_name in names:
        print(f"{entered_name} is in the list.")
    else:
        print(f"{entered_name} is not in the list.")
search_name(names, entered_name)  #Calling the search function











class Vending_Machine:
    def __init__(self): # Initialize the vending machine with categories of items.
        self.categories = {  # Creating dictionary to store item categories, codes, items, prices and stock.
            "Chocolates": {
                "A1": {"item": "Kit Kat", "price": 2.00, "stock": 10},
                "A2": {"item": "Kinder Bueno", "price": 4.50, "stock": 11},
                "A3": {"item": "Toblerone", "price": 4.00, "stock": 9},
                "A4": {"item": "Milka", "price": 5.00, "stock": 8},
            },
            "Chips": {
                "B1": {"item": "Lays Chilli", "price": 2.00, "stock": 8},
                "B2": {"item": "Buggles", "price": 1.00, "stock": 5},
                "B3": {"item": "Cheetos", "price": 3.50, "stock": 5},
                "B4": {"item": "Takis", "price": 4.00, "stock": 7},
            },
            "Drinks": {
                "C1": {"item": "Coca Cola", "price": 3.50, "stock": 6},
                "C2": {"item": "Pepsi", "price": 3.00, "stock": 10},
                "C3": {"item": "Mango Juice", "price": 2.00, "stock": 8},
                "C4": {"item": "Water", "price": 1.00, "stock": 6},
            },
            "Hot Drinks": {
                "D1": {"item": "Coffee", "price": 2.00, "stock": 5},
                "D2": {"item": "Tea", "price": 1.50, "stock": 5},
                "D3": {"item": "Hot Chocolate", "price": 2.25, "stock": 3},
            },
        }
        self.balance = 0.0 #Initializing balance to zero

    def menu(self):    #Displaying the menu of available items.
        print("Items available:")
        #Looping through categories and items to print them.
        for category, items in self.categories.items():
            print(f"\n{category}:")
            for code, details in items.items():
                print(f"{code}: {details['item']} - AED{details['price']:.2f} ({details['stock']} left)")

    def amount(self):    #Handling the insertion of money into the vending machine.
        try:
            amount = float(input("Enter the amount : AED")) #Asking user to enter the amount.
            if amount > 0:
                self.balance += amount #Updating balance once valid amount is entered.
                print(f"Balance updated: AED{self.balance:.2f}")
                proceed = input("Would you like to select an item now? (yes/no): ").strip().lower()
                if proceed == "yes":
                    self.item_code()
            else:
                print("Please enter a valid amount.") #Prints if user enters the wrong input.
        except ValueError:
            print("Invalid input. Please enter a number.")

    def item_code(self):
        code = input("Enter the item code: ").upper() #Asking user to enter the item code.
        #Looping through categories to find the item code.
        for category, items in self.categories.items():
            if code in items:
                item = items[code]
                if item['stock'] <= 0:
                    print(f"Oops Sorry, {item['item']} is out of stock.")  #Prints when the item is out of stock.
                    return
                if self.balance < item['price']:   #prints when fund is Insufficient.
                    print(f"Insufficient funds. {item['item']} costs AED{item['price']:.2f}.")
                    return  

            #for Deducting item price from balance and reduce stock.
                self.balance -= item['price']
                item['stock'] -= 1
                print(f"Dispensing {item['item']}. Remaining balance: AED{self.balance:.2f}")
                suggestion = self.suggestion(code) #Suggesting Complimentary items.
                if suggestion:
                    print(suggestion)
                return
        print("Invalid item code. Please try again.")

    def suggestion(self, code): #Suggesting complementary items based on selected item code.
        suggestions = {
            "A1": "Why not pair a drink with your Kit Kat?",
            "A2": "Kinder Bueno and Water make a great combo!",
            "A3": "umm,Toblerone goes great with water!",
            "A4": "Great choice! why not go for drinks.",
            "B1": "Lays with coca cola.Perfect combination.",
            "B2": "Buggles perfectly pair with tea.",
            "B3": "Wow, the spice! Try some Mango Juice.",
            "B4": "Takis and water go well perfectly!",
            "C1": "Coca cola?? you will love it with lays.",
            "C2": "Pepsi pairs perfectly with Cheetos",
            "C3": "Mango juice with kit kats is delightful",
            "C4": "Just water alone? Add some chips to make a full meal.",
            "D1": "hmm Coffee goes well with buggles",
            "D2": "Tea and chips go well together",
            "D3": "Try Hot Chocolate with Milka! Sweet pairing."
        }
        return suggestions.get(code)

    def change(self):   #Handling the return of change.
        if self.balance > 0:
            print(f"Returning AED{self.balance:.2f} in change.")
            self.balance = 0.0  #Reseting balance to zero.
        else:
            print("No change to return.")

    def run(self):  #Main loop to run the vending machine program.
        while True:
            print("\nHi!! Very welcome to sahara's best vending Machine!")
            print("I bet you will love to purchase from here hehe.")
            self.menu()
            print("\nOptions:")
            print("1. Insert your money here")
            print("2. Select your favourite Item")
            print("3. Returning Changes")
            print("4. Exit")

            choice = input("Hey! Choose an option: ") #Asking user to choose from the given option.
            if choice == "1":
                self.amount()
            elif choice == "2":
                self.item_code()
            elif choice == "3":
                self.change()
            elif choice == "4":
                self.change()
                print("Thank you for using my vending machine!\nIt was lovely to have you.")
                break
            else:
                print("Invalid option. Please choose again.")


# To run the Vending Machine program.
if __name__ == "__main__":
    vending_machine = Vending_Machine()
    vending_machine.run() 

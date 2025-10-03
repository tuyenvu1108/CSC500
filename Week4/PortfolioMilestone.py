# Global variables
center_text = 30
item_num = 2

# This function is taking a string and output it with cernter aligned
def printCenter(output_str):
    print(output_str.center(center_text))

# Item class
class ItemToPurchase:
    # Contructor
    def __init__(self, name = 'none', price = 0, quantity = 0):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_total = self.item_quantity * self.item_price
    
    # This function output the cost of item
    def print_item_cost(self):
        printCenter(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_total}")

# This function is getting item's name, validating, and return it
def getName():
    while True:
        try:
            # Get input
            printCenter('Enter the item name:')
            name = input('\t')
            # Validating quantity input
            if (name == ''):
                raise ValueError
            return name
        except ValueError:
            # Catching error when entering in valid input
            printCenter('Invalid input. Please try again.')

# This function is getting item's price, validating, and return it
def getPrice():
    while True:
        try:
            # Get user input
            printCenter('Enter the item price:')
            num = float(input("\t"))
            # Do not accept negative number
            if (num < 0):
                raise ValueError
            return num
        except ValueError:
            # Catching error when entering in valid input
            printCenter('Invalid input. Please try again.')

# This function is getting item's quantity, validating, and return it
def getQuantity():
    while True:
        try:
            # Get input
            printCenter('Enter the item quantity:')
            num = int(input("\t"))
            # Validating quantity input
            if (num <= 0):
                raise ValueError
            return num
        except ValueError:
            # Catching error when entering in valid input
            printCenter('Invalid input. Please try again.')



if __name__ == "__main__":
    cart = []
    for i in range (1, item_num + 1):
        print()
        printCenter(f'Item {i}')
        
        # Get item information
        item_name = getName()
        item_price = getPrice()
        item_quantity = getQuantity()

        # Create item object
        item = ItemToPurchase(item_name, item_price, item_quantity)
        # Add item to cart
        cart.append(item)
    
    total = 0
    # Print total information
    print()
    printCenter("TOTAL COST")
    for item in cart:
        total += item.item_total
        item.print_item_cost()
    printCenter(f"Total: ${total}")
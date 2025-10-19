# Global variables
center_text = 30
item_num = 2

# This function is taking a string and output it with cernter aligned
def printCenter(output_str):
    print(output_str.center(center_text))

# This function is displaying menu and getting user choice
def print_menu(cart):
    choice = ''
    choiceOptions = ['a', 'r', 'c', 'i', 'o', 'q']
    while (choice != 'q'):
        print()
        printCenter('MENU')
        printCenter('a - Add item to cart')
        printCenter('r - Remove item from cart')
        printCenter('c - Change item quantity')
        printCenter("i - Output items' descriptions")
        printCenter('o - Output shopping cart')    
        printCenter('q - Quit')
        printCenter('Choose an option:')
        # Validating input
        choice = input('\t').lower()
        if choice not in choiceOptions:
            printCenter('Invalid choice. Please try again.')
            continue

# Building classes
class ItemToPurchase:
    # Contructor
    def __init__(self, name = 'none', description = 'none', price = 0, quantity = 0):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity
        self.item_total = self.item_quantity * self.item_price
    
    # This function output the cost of item
    def print_item_cost(self):
        printCenter(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_total}")

    # This function output the description of item
    def print_item_description(self):
        printCenter(f"{self.item_name}: {self.item_description}")

class ShoppingCart:
    # Contructor
    def __init__(self, name = 'none', date = 'January 1, 2020', items = []):
        self.customer_name = name
        self.current_date = date
        self.cart_items = items
    
    # This function is taking an ItemToPurchase and add to the cart
    def add_item(self, item):
        self.cart_items.append(item)

    # This function taking item's name and remore it from the cart
    def remove_item(self, name):
        for i in range(0, len(self.cart_items)):
            if (self.cart_items[i].item_name == name):
                self.cart_items.pop(i)
                break
        else:
            print('Item not found in cart. Nothing removed.')

    # This function is taking an ItemToPurchase and modify the matched existing item in the cart
    def modify_item(self, item):
        for i in range(0, len(self.cart_items)):
            if (self.cart_items[i].item_name == item.item_name):
                if (item.item_description != 'none'):
                    self.cart_items[i].item_description = item.item_description
                if (item.item_price != 0):
                    self.cart_items[i].item_price = item.item_price
                if (item.item_quantity != 0):
                    self.cart_items[i].item_quantity = item.item_quantity
                break
        else:
            print('Item not found in cart. Nothing modified.')       

    # This function is returning the number of item in the cart
    def get_num_items_in_cart(self):
        return len(self.cart_items)

    # This function is calculating and returning the total cost of items in the cart
    def get_cost_of_cart(self):
        total_cost = 0

        for item in self.cart_items:
            total_cost += item.item_total

        return total_cost

    # This function output the total of objects in the cart
    def print_total(self):
        itemCount = self.get_num_items_in_cart()
        if (itemCount):
            print()
            printCenter(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            printCenter(f"Number of Items: {itemCount}")
            for item in self.cart_items:
                item.print_item_cost()
            total = self.get_cost_of_cart()
            printCenter(f"Total: ${total}")
        else:
            print('SHOPPING CART IS EMPTY')

    # This function output each item's description
    def print_descriptions(self):
        if (len(self.cart_items)):
            print()
            printCenter(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            printCenter('Item Descriptions')
            for item in self.cart_items:
                item.print_item_description()
        else:
            print('SHOPPING CART IS EMPTY')

if __name__ == "__main__":
    # Testing empty cart
    print('Empty cart testing......')
    cart = ShoppingCart('Tuyen Vu', 'October 19, 2025')
    print_menu(cart)
    cart.print_total()
    cart.print_descriptions()
    cart.remove_item('Nike Romaleos')
    cart.modify_item(ItemToPurchase())

    # Add an item to the empty cart
    print()
    print('Add item testing......')
    cart.add_item(ItemToPurchase('Nike Romaleos', 'Volt color, Weightlifting shoes', 189, 2))
    cart.print_total()

    # Modify the existing item
    print()
    print('Modify item testing.......')
    cart.modify_item(ItemToPurchase('Nike Romaleos', 'none', 200, 1))
    cart.print_total()

    # Remove the existing item
    print()
    print('Remove item testing......')
    cart.remove_item('Nike Romaleos')
    cart.print_total()

    # Create new cart with items
    print()
    print('Cart with items testing......')
    cart_items = [
        ItemToPurchase('Nike Romaleos', 'Volt color, Weightlifting shoes', 189, 2),
        ItemToPurchase('Chocolate Chips', 'Semi-sweet', 3, 5),
        ItemToPurchase('Powerbeats 2 Headphones', 'Bluetooth headphones', 128, 1)
    ]
    cart = ShoppingCart('Tuyen Vu', 'October 19, 2025', cart_items)
    cart.print_total()
    cart.print_descriptions()
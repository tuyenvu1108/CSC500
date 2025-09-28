# Write a program that calculates the total amount of a meal purchased at a restaurant. 
# The program should ask the user to enter the charge for the food 
#   and then calculate the amounts with an 18 percent tip and 7 percent sales tax. 
# Display each of these amounts and the total price.

# This function is returning user input for purchased amount
def getPurchasedAmount():
    while True:
        try:
            # Get user input
            num = float(input('Enter the purchased amount total: $'))
            # Do not accept negative number
            if (num < 0):
                raise ValueError
            return num
        except ValueError:
            # Catching error when entering in valid input
            print('Invalid input. Please try again.')

if __name__ == "__main__":
    # Get input
    purchasedAmount = getPurchasedAmount()
    # Calculate tip and tax
    tipAmount = 0.18 * purchasedAmount
    taxAmount = 0.07 * purchasedAmount
    total = purchasedAmount + tipAmount + taxAmount

    # Display results
    print()
    print('=========Transaction Details==========')
    print('Subtotal: \t$', purchasedAmount)
    print('Tip: \t\t$', tipAmount)
    print('Tax: \t\t$', taxAmount)
    print('=======================')
    print('Total: \t\t$', total)
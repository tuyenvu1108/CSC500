# Write a Python program to find the multiplication and division of two numbers.
# Ask the user to input two numbers (num1 and num2). Given those two numbers, multiply them together to find the output. Also, divide num1/num2 to find the output.

def getNumberInput():
    while True:
        try:
            num = float(input('Enter a number: '))
            return num
        except ValueError:
            print('Invalid input. Please try again.')

if __name__ == "__main__":
    num1 = getNumberInput()
    num2 = getNumberInput()
    print('Multiplication result: ', num1 * num2)
    if (num2 == 0):
        print('Cannot perform division by zero.')
    else:
        print('Division result: ', num1 / num2)
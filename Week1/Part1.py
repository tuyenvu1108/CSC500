# Write a Python program to find the addition and subtraction of two numbers.
# Ask the user to input two numbers (num1 and num2). Given those two numbers, add them together to find the output. Also, subtract the two numbers to find the output.

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
    print('Addition result: ', num1 + num2)
    print('Subtraction result: ', num1 - num2)
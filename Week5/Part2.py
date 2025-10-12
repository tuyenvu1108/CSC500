# The CSU Global Bookstore has a book club that awards points to its students based on the number of books purchased each month. 
# The points are awarded as follows:
# If a customer purchases 0 books, they earn 0 points.
# If a customer purchases 2 books, they earn 5 points.
# If a customer purchases 4 books, they earn 15 points.
# If a customer purchases 6 books, they earn 30 points.
# If a customer purchases 8 or more books, they earn 60 points.
# Write a program that asks the user to enter the number of books that they have purchased this month and then display the number of points awarded.

# This function is returning user input for number of books purchased this month
def getBooks():
    while True:
        try:
            # Get user input
            num = int(input('Enter the number of books purchased this month: '))
            # Do not accept negative number
            if (num < 0):
                raise ValueError
            return num
        except ValueError:
            # Catching error when entering in valid input
            print('Invalid input. Please try again.')

# This function is taking the number of books purchased and return the points awarded 
def getPoints(books):
    if (books < 2):
        return 0
    elif (books < 4):
        return 5
    elif (books < 6):
        return 15
    elif (books < 8):
        return 30
    else:
        return 60

if __name__ == "__main__":
    books = getBooks()
    points = getPoints(books)
    print('Congratulation! You have earned %s points' % points)

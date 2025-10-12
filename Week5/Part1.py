# Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. 
# The program should first ask for the number of years. 
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.
# Each iteration of the inner loop will ask the user for the inches of rainfall for that month. 
# After all iterations, the program should display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period.

# This function is returning user input for number of years
def getYears():
    while True:
        try:
            # Get user input
            num = int(input('Enter the number of years in the period: '))
            # Do not accept negative number
            if (num < 0):
                raise ValueError
            return num
        except ValueError:
            # Catching error when entering in valid input
            print('Invalid input. Please try again.')

# This function is returning user input for rainfall amount
def getRainfall():
    while True:
        try:
            # Get user input
            num = float(input('Enter the inches of rainfall: '))
            # Do not accept negative number
            if (num < 0):
                raise ValueError
            return num
        except ValueError:
            # Catching error when entering in valid input
            print('Invalid input. Please try again.')


if __name__ == "__main__":
    totalRainfall = 0
    years = getYears()

    # Looping over years
    for i in range (1, years + 1):
        print()
        print('Year ', i)
        # Looping over months
        for j in range (1, 13):
            print('Month ', j)
            rainfall = getRainfall()
            totalRainfall += rainfall
    
    # Calculate average rainfall
    totalMonths = years * 12
    averageRainfall = totalRainfall / totalMonths
    print()
    print('Rainfall Summary for the Period')
    print('Number of months: ', totalMonths)
    print('Total inches of rainfall: %.2f' % totalRainfall)
    print('Average rainfall per month: %.2f' % averageRainfall)

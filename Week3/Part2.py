# Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
# Write a Python program to solve the general version of the above problem. 
# Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm. 
# Your program should output what the time will be on a 24-hour clock when the alarm goes off.

# This funtion is returning the time now (in hours)
def getTime():
    while True:
        try:
            # Get input
            num = int(input('Enter current time (in hours 0-23): '))
            # Validating time input
            if (num < 0 or num > 23):
                raise ValueError
            return num
        except ValueError:
            print('Invalid input. Please try again.')

# This function is returning the amount of waiting time before alarm goes off
def getAlarmHours():
    while True:
        try:
            # Get input
            num = int(input('The alarm will go off in (hours): '))
            # Validating input
            if (num < 0):
                raise ValueError
            return num
        except ValueError:
            print('Invalid input. Please try again.')

if __name__ == "__main__":
    # Get inputs
    currentTime = getTime()
    alarmHours = getAlarmHours()

    # Calculate the time when the alarm should goes off
    remainder = alarmHours % 24
    alarmTime = currentTime + remainder

    # Handling the case where the time goes pass 24 hours
    if (alarmTime >= 24):
        alarmTime = abs(alarmTime - 24)
    
    print('The alarm will go off at %d:00' %(alarmTime))

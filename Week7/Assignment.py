# This function is returning 3 dictionaries containing courses' information
def createCourseInfo():
    roomDict = {
        'CSC101': 3004,
        'CSC102': 4501,
        'CSC103': 6755,
        'NET110': 1244,
        'COM241': 1411
    }

    instructorDict = {
        'CSC101': 'Haynes',
        'CSC102': 'Alvarado',
        'CSC103': 'Rich',
        'NET110': 'Burke',
        'COM241': 'Lee'
    }

    timeDict = {
        'CSC101': '8:00 a.m.',
        'CSC102': '9:00 a.m.',
        'CSC103': '10:00 a.m.',
        'NET110': '11:00 a.m.',
        'COM241': '1:00 p.m.'
    }
    return roomDict, instructorDict, timeDict

if __name__ == "__main__":
    # List of keys
    courseNumbers = ['CSC101', 'CSC102', 'CSC103', 'NET110', 'COM241']
    # Get courses' information'
    roomDict, instructorDict, timeDict = createCourseInfo()

    courseNumber = input('Enter the course number to see more information: ')
    if (courseNumber in courseNumbers):
        # Output course's details
        print('Room: ', roomDict[courseNumber])
        print('Instructor: ', instructorDict[courseNumber])
        print('Meeting time: ', timeDict[courseNumber])
    else:
        print('%s does not exist!' % courseNumber)
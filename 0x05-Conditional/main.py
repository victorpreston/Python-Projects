# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.




4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function. 

def getAttr():
    finalScore = ""
    userScore = float(input("Enter your score between 0.0 and 1.0"))
    while userScore > 1.0 or userScore < 0.0:
        print("Error")
        userScore = float(input("Enter your score between 0.0 and 1.0"))
        if userScore > 0.0 and userScore < 1.0:
            break

    if userScore >= 0.9:
        finalScore = "A"
    elif userScore >= 0.8:
        finalScore = "B"
    elif userScore >= 0.7:
        finalScore = "C"
    elif userScore >= 0.6:
        finalScore = "D"
    elif userScore < 0.6:
        finalScore = "F"
    print(finalScore)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    getAttr()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

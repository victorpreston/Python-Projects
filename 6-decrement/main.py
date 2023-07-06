# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Write
# a
# program
# that
# repeatedly
# prompts
# a
# user
# for integer numbers until the user enters 'done'.Once 'done' is entered,
# print out the largest and smallest of the numbers.If the user enters anything
# other than a valid number catch it with a try / except and put out an appropriate
# message and ignore the number.Enter 7, 2, bob, 10, and 4 and match the output below.

def prompt():
    try:
        print(
            "Hello , you should enter each time an integer till you enter done, then we will provide you the maximal value and the minimal value")
        user_min = 0
        user_max = 0
        user_array = []
        user_input = ""

        user_input = input("Enter a number, enter done if you want to stop")
        user_min = int(user_input)
        while user_input != "done":
            print(user_input)
            #       user_array += user_input
            if int(user_input) < user_min:
                user_min = int(user_input)
                print("all new min is :", user_min)
            if int(user_input) > user_max:
                user_max = int(user_input)
                print("all new max is :", user_max)
            user_input = input("Enter a number, enter done if you want to stop")
            if user_input == "done":
                print("over")

                print("min value is ", user_min)
                print("max value is :", user_max)
                break

    except:
        print("Error, you should enter a number")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    prompt()
else:
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

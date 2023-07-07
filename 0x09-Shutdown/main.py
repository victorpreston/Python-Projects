# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def systemOffRestart():
    import os
    print("enter r for restart")
    print("enter s for shutdown")
    print("enter any key for exot")

    option = input("enter your option")
    if option == "r":
        os.system('shutdown /r')
    elif option == "s":
        os.system('shutdown /s')
    else:
        exit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    systemOffRestart()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

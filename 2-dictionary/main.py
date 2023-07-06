# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json


def dic():
    data = json.load(open("data.json"))
    print(data["smog"])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dic()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

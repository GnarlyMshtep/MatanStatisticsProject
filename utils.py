# def sort...

from typing import Iterable
numbericalChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']


def insort(arr: list, item):
    for i in range(len(arr)):
        if arr[i] >= item:
            arr.insert(i, item)
            return
    arr.append(item)


def stringToList(str: str) -> list:
    list = []
    tempStr = ""
    for char in str:
        if char in numbericalChars:
            tempStr += char
        elif len(tempStr) != 0:
            list.append(float(tempStr))
            tempStr = ""
    return list

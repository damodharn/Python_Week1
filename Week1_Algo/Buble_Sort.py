# *********************************************************************************************
# Purpose: To Read in integers prints them in sorted order using Bubble Sort.
# Author:  Damodhar D. Nirgude.
#  ************************************************************************************************
from Week1_Algo.Utility2 import Utility2


arr = []
try:
    lent = int(input("Enter the length of an array"))
except ValueError as e:
    print("Plz Enter only integer\n", e)
else:
    try:
        print("Enter Elements of an Array")
        for x in range(lent):
            arr.append(int(input()))
    except ValueError as e:
        print("Plz Enter only integer\n", e)
    else:
        print("u've Entered")
        print(arr)
        Utility2.bubbleSortInt(arr, lent)

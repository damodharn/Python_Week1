# *********************************************************************************************
# Purpose: To Read in strings from standard input and prints them in sorted order using insertion sort.
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
        Utility2.insertionSort_int(arr, lent)

# *********************************************************************************************
# Purpose: To Read in strings from standard input and prints them in sorted order using insertion sort.
# Author:  Damodhar D. Nirgude.
#  ************************************************************************************************
from Week1_Algo.Utility2 import Utility2


arr = []
lent = int(input("Enter the length of an array"))
print("Enter Elements of an Array")
for x in range(lent):
    arr.append(input())
print("u've Entered")
print(arr)
Utility2.insertionSort_int(arr, lent)

# *********************************************************************************************
# Purpose: To Read in integers prints them in sorted order using Bubble Sort.
# Author:  Damodhar D. Nirgude.
#  ************************************************************************************************
from Week1_Algo.Utility2 import Utility2


arr = []
lent = int(input("Enter the length of an array"))
print("Enter Elements of an Array")
for x in range(lent):
    arr.append(int(input()))
print("u've Entered")
print(arr)
Utility2.bubbleSortInt(arr, lent)

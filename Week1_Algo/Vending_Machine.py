# *********************************************************************************************
# Purpose: To Read in integers prints them in sorted order using Bubble Sort.
# Author:  Damodhar D. Nirgude.
#  ************************************************************************************************
from Week1_Algo.Utility2 import Utility2


arr = [1000, 500, 100, 50, 10, 5, 2, 1]
total = 0
i = 0
amt = int(input("Enter an Amount u wanted to withdraw"))
total = Utility2.vending_machine(arr, amt, total, i)
print("Total No. of Notes Required are : ", total)

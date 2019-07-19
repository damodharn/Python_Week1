# *********************************************************************************************
# Purpose: Program for various Sorting techniques and Binary search.
# Author:  Damodhar D. Nirgude.
# Version: 3.1
#  ************************************************************************************************
from Week1_Algo.Utility2 import Utility2
no = 8  # To enter into the while loop
while no != 7:  # To come out of the loop(Enter only 7)
    no = int(input("Enter ur choice:\n1: binarySearch method for integer\n"
                   "2: binarySearch method for String\n3: insertionSort method for integer\n"
                   "4: insertionSort method for String\n5: bubbleSort method for integer\n"
                   "6: bubbleSort method for String\n7: exit"))
    if no == 1:
        Utility2.binarySearchInt()
    elif no == 2:
        Utility2.binarySearchString()
    elif no == 3:
        Utility2.insertionSort_int()
    elif no == 4:
        Utility2.insertionSort_string()
    elif no == 5:
        Utility2.bubbleSortInt()
    elif no == 6:
        Utility2.bubbleSortString()
    else:
        if no == 7:
            break
        else:
            print("Wrong Entry....Enter Valid choice")

# *********************************************************************************************
# Purpose: Program for various Sorting techniques and Binary search.
# Author:  Damodhar D. Nirgude.
#  ************************************************************************************************
from Week1_Algo.Utility2 import Utility2
no = 8  # To enter into the while loop
while no != 7:  # To come out of the loop(Enter only 7)
    no = int(input("Enter ur choice:\n1: binarySearch method for integer\n"
                   "2: binarySearch method for String\n3: insertionSort method for integer\n"
                   "4: insertionSort method for String\n5: bubbleSort method for integer\n"
                   "6: bubbleSort method for String\n7: exit \nEnter ur choice: "))

    #  **********************  Binary Search Int  ************************************
    if no == 1:
        len = int(input("Enter a length of an array"))
        arr = []
        print("Enter array elements")
        for i in range(len):
            arr.append(int(input()))
        print("U've Entered")
        print(arr)
        no = int(input("Enter a No. to be Searched"))
        Utility2.binarySearchInt(arr, no)

    #  ************************** Binary Search String  ***************************
    elif no == 2:
        len = int(input("Enter a length of an array"))
        arr = []
        print("Enter array elements")
        for i in range(len):
            arr.append(input())
        print("U've Entered")
        print(arr)
        str = input("Enter a string to be Searched")
        Utility2.binarySearchString(arr, len, str)

    #  *************************  Insertion Sort Int  *************************
    elif no == 3:
        len = int(input("Enter the array length"))
        arr = []
        print("Enter the elements of an Array")
        for i in range(len):
            arr.append(int(input()))
        print("U've Entered :")
        print(arr)
        Utility2.insertionSort_int(arr, len)

    #  ************************  Insertion Sort String  *********************
    elif no == 4:
        len = int(input("Enter the array length"))
        arr = []
        print("Enter the elements of an Array")
        for i in range(len):
            arr.append((input()))
        print("U've Entered :")
        print(arr)
        Utility2.insertionSort_string(arr, len)

    #  **************************  Bubble Sort Int  ***************************
    elif no == 5:
        len = int(input("Enter a length of an array"))
        arr = []
        print("Enter array elements")
        for i in range(len):
            arr.append(int(input()))
        print("U've Entered")
        print(arr)
        Utility2.bubbleSortInt(arr, len)

    #  *****************************  Bubble Sort String  ***********************
    elif no == 6:
        len = int(input("Enter a length of an array"))
        arr = []
        print("Enter array elements")
        for i in range(len):
            arr.append(input())
        print("U've Entered")
        print(arr)
        Utility2.bubbleSortString(arr, len)
    else:
        if no == 7:
            break
        else:
            print("Wrong Entry....Enter Valid choice")

# *********************************************************************************************
# Purpose: To create an Utility class for all static methods of Algorithmic programs.
# Author:  Damodhar D. Nirgude.
# Version: 3.1
#  ************************************************************************************************
from array import array
import time

class Utility2:

    @staticmethod
    def primeno():
        count = 0
        for x in range(2, 1000):
            prime = 1
            count += 1
            for y in range(2, (x // 2) + 1):
                if x % y == 0:
                    prime = 0
                    count -= 1
                    break
            if prime == 1:
                if (count - 1) % 10 == 0:
                    print("\n")
                print(count, ')', x, "", end="")

    # #################################  Prime  Anagram #######################
    @staticmethod
    def primeAnagram(no: object) -> object:                         # Method to Check Prime No.
        arr = array('i', [])
        arr2 = array('i', [])
        count = 0
        for i in range(2, no + 1):
            prime = 1
            count += 1
            for j in range(2, i // 2 + 1):
                if i % j == 0:
                    prime = 0
                    count -= 1
                    break
            if prime == 1:
                arr.append(i)
                arr2.append(i)
            #  ****************************  Anagram checking    ********************************

        print('\n*********************  Prime Anagrams  **************************************\n')
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                if len(str(arr[i])) == len(str(arr[j])):
                    var1 = ''.join(sorted(str(arr[i])))
                    var2 = ''.join(sorted(str(arr[j])))
                    if var1 == var2:
                        print(arr[i], 'and', arr[j], 'are Anagrams')

    #  *************************** Pelindrome check   *******************************************
        print('\n**************  Prime Palindromes *********************************************\n')
        for i in range(len(arr2)):
            if arr[i] > 10:
                no = arr[i]
                rev = 0
                temp = 0
                while no != 0:
                    temp = no % 10
                    rev = rev*10+temp
                    no = no // 10
                if arr[i] == rev:
                    print(arr[i], 'is a Palindrome')
        #  *************************  String Anagram  **********************************8
    @staticmethod
    def stringanagram(str1, str2):
        str1 = sorted(str1)
        str2 = sorted(str2)
        if str1 == str2:
            print('Strings are anagram')
        else:
            print('strings are not Anagrams')

    #  *************************** Insertion Sort For Integer  **************************

    @staticmethod
    def insertionSort_int():
        len = int(input("Enter the array length"))
        arr = []
        print("Enter the elements of an Array")
        for i in range(len):
            arr.append(int(input()))
        print("U've Entered :")
        print(arr)
        print("After sorting Array: ")
        startTime = time.time()
        for i in range(1, len):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j = j-1
                arr[j+1] = key
        print(arr)
        stopTime = time.time()
        elapsedTime = stopTime - startTime
        print("Time Elapsed", elapsedTime, "sec\n")

    #  *************************** Insertion Sort For String  **************************
    @staticmethod
    def insertionSort_string():
        len = int(input("Enter the array length"))
        arr = []
        print("Enter the elements of an Array")
        for i in range(len):
            arr.append((input()))
        print("U've Entered :")
        print(arr)
        print("After sorting Array: ")
        startTime = time.time()
        for i in range(1, len):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j = j - 1
                arr[j + 1] = key
        print(arr)
        stopTime = time.time()
        elapsedTime = stopTime - startTime
        print("Time Elapsed", elapsedTime, "sec\n")

    #  *************************** Bubble Sort For Integer  **************************
    @staticmethod
    def bubbleSortInt():
        len = int(input("Enter a length of an array"))
        arr = []
        print("Enter array elements")
        for i in range(len):
            arr.append(int(input()))
        print("U've Entered")
        print(arr)
        print("Sorted array is: ")
        startTime = time.time()
        for i in range(len):
            for j in range(0, len-i-1):
                if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
        print(arr)
        stopTime = time.time()
        elapsedTime = stopTime - startTime
        print("Time Elapsed is: ", elapsedTime, "sec\n")

    #  *************************** Bubble Sort For String  **************************

    @staticmethod
    def bubbleSortString():
        len = int(input("Enter a length of an array"))
        arr = []
        print("Enter array elements")
        for i in range(len):
            arr.append(input())
        print("U've Entered")
        print(arr)
        print("Sorted array is: ")
        startTime = time.time()
        for i in range(len):
            for j in range(0, len - i - 1):
                if arr[j] > arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
        print(arr)
        stopTime = time.time()
        elapsedTime = stopTime - startTime
        print("Time Elapsed is: ", elapsedTime, "sec\n")

    #  *************************** Binary Search For Integer  **************************
    @staticmethod
    def binarySearchInt():
        len = int(input("Enter a length of an array"))
        arr = []
        print("Enter array elements")
        for i in range(len):
            arr.append(int(input()))
        print("U've Entered")
        print(arr)
        print("Sorted array is: ")
        for i in range(1, len):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j = j - 1
                arr[j + 1] = key
        print(arr)
        low = 0
        high = len - 1
        mid = (low + high)//2
        no = int(input("Enter a No. to be Searched"))
        startTime = time.time()
        while low <= high:
            if arr[mid] == no:
                print("No. is Found at ", mid+1, "th Position in an Array\n")
                break
            elif arr[mid] < no:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high)//2
        if low > high:
            print("Given no", no, " not found in an array\n")
        stopTime = time.time()
        elapsedTime = stopTime - startTime
        print("Time Elapsed is: ", elapsedTime, "sec\n")

        #  *************************** Binary Search For String  **************************
    @staticmethod
    def binarySearchString():
        len = int(input("Enter a length of an array"))
        arr = []
        print("Enter array elements")
        for i in range(len):
            arr.append(input())
        print("U've Entered")
        print(arr)
        print("Sorted array is: ")
        for i in range(1, len):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j = j - 1
                arr[j + 1] = key
        print(arr)
        low = 0
        high = len - 1
        mid = (low + high) // 2
        str = input("Enter a string to be Searched")
        startTime = time.time()
        while low <= high:
            if arr[mid] == str:
                print("String", str, " is Found at ", mid + 1, "th Position in an Array\n")
                break
            elif arr[mid] < str:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2
        if low > high:
            print("Given string", str, " not found in an array\n")
        stopTime = time.time()
        elapsedTime = stopTime - startTime
        print("Time Elapsed is: ", elapsedTime, "sec\n")

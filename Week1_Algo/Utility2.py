# *********************************************************************************************
# Purpose: To create an Utility class for all static methods of Algorithmic programs.
# Author:  Damodhar D. Nirgude.
#  ************************************************************************************************
from array import array
import time
import sys
import math
sys.setrecursionlimit(5000)

class Utility2:

    #  *******************************  Prime No.  **************************************************
    @staticmethod
    def primeno():
        count = 0  # Taking count for printing prime no in Proper alignment
        for x in range(2, 1000):  #
            prime = 1
            count += 1
            for y in range(2, (x // 2) + 1):  # dividing no x by each no which are less than or equal to it's half.
                if x % y == 0:
                    prime = 0
                    count -= 1
                    break
            if prime == 1:
                if (count - 1) % 10 == 0:  # Changing Line after printing 10 prime No's.
                    print("\n")
                print(count, ')', x, "")

# #################################  Prime  Anagram #######################
    #  *****************************  String Anagram  ***********************************
    @staticmethod
    def stringanagram(str1, str2):
        str1 = sorted(str1)
        str2 = sorted(str2)
        if str1 == str2:  # comparing the sorted string, if found same then strings are anagram.
            print('Strings are anagram')
        else:
            print('strings are not Anagrams')

#  *************************** Insertion Sort For Integer  **************************

    @staticmethod
    def insertionSort_int(arr, len):
        print("After sorting Array: ")
        startTime = time.time()
        for i in range(1, len):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:  #
                arr[j+1] = arr[j]
                j = j-1
                arr[j+1] = key
        print(arr)
        stopTime = time.time()
        elapsedTime = stopTime - startTime
        print("Time Elapsed", elapsedTime, "sec\n")

#  *************************** Insertion Sort For String  **************************
    @staticmethod
    def insertionSort_string(arr, len):
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
    def bubbleSortInt(arr, len):

        print("Sorted array is: ")
        startTime = time.time()
        for i in range(len):
            for j in range(len-i-1):
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
    def bubbleSortString(arr, len):
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
    def binarySearchInt(arr, no):
        lent = len(arr)
        for i in range(1, lent):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j = j - 1
                arr[j + 1] = key
        print("Sorted array is: ")
        print(arr)
        low = 0
        high = lent - 1
        mid = (low + high)//2

        startTime = time.time()
        while low <= high:
            if arr[mid] == no:
                print("No. is Found at ", mid+1, "th Position in sorted Array\n")
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
    def binarySearchString(arr, len, str):

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
        startTime = time.time()
        while low <= high:
            if arr[mid] == str:
                print("String", str, " is Found at", mid + 1, "th Position in sorted  Array\n")
                break
            elif arr[mid] < str:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2
        if low > high:
            print("Given string", str, "not found in an array\n")
        stopTime = time.time()
        elapsedTime = stopTime - startTime
        print("Time Elapsed is: ", elapsedTime, "sec\n")

#  *****************************  Guess the No  ******************************
    @staticmethod
    def guess_no(no):
        cnt = 0
        len = int(no)
        arr = []
        for i in range(len):
            arr.append(i)   # Creating array of No. upto given no-1
    #  Using Binary search to Guess the No. of User
        low = 0
        high = len-1
        mid = (low + high)//2
        while low <= high:
            cnt = cnt+1  # To calculate No. of Questions asked.
            print(arr[mid])
            print("Is this Ur No.\n 1: True 2: False")  # asking user about his/her no by showing array[mid] no.
            choice = int(input())
            if choice == 1:
                print("Hurrey...I found ur No after", cnt, "questions")
                break
            elif choice == 2:
                print("Is ur No larger than than", arr[mid], "\nEnter 1: True 2: False")
                choice2 = int(input())
                if choice2 == 1:
                    low = mid + 1
                elif choice2 == 2:
                    high = mid - 1
                else:
                    print("Wrong entry")
                mid = (low + high)//2
            else:
                print("wrong choice")
        if low > high:
            print("U gave some wrong answer/s\n")

# #################################  Prime  Anagram #######################
    @staticmethod
    def primeAanagram(no):                         # Method to Check Prime No.
        arr = array('i', [])  # Array to store prime no.
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
                arr.append(i)  # Storing each prime no. after the last added no. in an array.

                arr2.append(i)
        #  ***********************   Anagram checking    ******************

        print('\n*********************  Prime Anagrams  **************************************\n')
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                if len(str(arr[i])) == len(str(arr[j])):
                    var1 = ''.join(sorted(str(arr[i])))  # Making array element a string
                    var2 = ''.join(sorted(str(arr[j])))
                    if var1 == var2:
                        print(arr[i], 'and', arr[j], 'are Anagrams')

        #  *************************** Palindrome check   *******************************************
        print('\n**************  Prime Palindromes *********************************************\n')
        for i in range(len(arr2)):
            if arr[i] > 10:
                nu = arr[i]
                rev = 0
                temp = 0
                while nu > 0:
                    temp = nu % 10
                    rev = rev * 10 + temp
                    nu = nu // 10

                if arr[i] == rev:
                    print(arr[i], 'is prime Palindrome')

#  ********************************  Vending Machine  ****************************************
    @staticmethod
    def vending_machine(arr, amt, sum, i):
        if amt == 0:
            return sum
        if amt >= arr[i]:
            note = amt // arr[i]  # Counting No. of notes of particular amount.
            amt = amt % arr[i]  # Updating new amount after removing higher value notes.
            sum = sum + note  # Updating total count of the Notes into the variable sum.
            print(arr[i], "Rs. Notes: ", note)
        i = i + 1
        sum = Utility2.vending_machine(arr, amt, sum, i)  #
        return sum
#  ******************************  Day of Week  ***********************************************
    @staticmethod
    def day_of_week(d, m, y):
        y0 = y - (14 - m) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + 31 * m0 // 12) % 7
        if d0 == 0:
            print("Sunday")
        if d0 == 1:
            print("Monday")
        if d0 == 2:
            print("Tuesday")
        if d0 == 3:
            print("Wednesday")
        if d0 == 4:
            print("Thursday")
        if d0 == 5:
            print("Friday")
        if d0 == 6:
            print("Saturday")

#  ***************************  Temperature Conversion  ******************************
    @staticmethod
    def tempconvert(case, temp):
        if case == 1:
            f = (temp * 9//5) + 32  # Formula for Celsius to Fahrenheit conversion.
            return f
        else:
            c = (temp - 32) * 5/9  # Formula for  Fahrenheit to Celsius conversion.
            return c
#  *****************************  Square Root of a No.  ******************************
    @staticmethod
    def sqrt(no):
        t = no
        epsilon = 1e-15
        while abs(t - no/t) > epsilon * t:
            t = (no // t + t) // 2
        return t

# *********************************************************************************************
# Purpose: Program for checking if two strings are Anagram or not.
# Author:  Damodhar D. Nirgude.
#  ************************************************************************************************
from Week1_Algo.Utility2 import Utility2

temp = int(input("Input Temperature"))
while 1:
    print("Select Conversion:\n1: Celsius to Fahrenheit\n2: Fahrenheit to Celsius")
    choice = int(input())
    if choice == 1 or choice == 2:
        converted = Utility2.tempconvert(choice, temp)
        print("Converted temp: ", converted)
        break
    else:
        print("Wrong I/p")

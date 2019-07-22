# *********************************************************************************************
# Purpose: Program for checking if two strings are Anagram or not.
# Author:  Damodhar D. Nirgude.
#  ************************************************************************************************
from Week1_Algo import Utility2

temp = int(input("Input Temperature"))
while choice != 1 or choice != 2:
    print("Select Conversion:\n1: Celsius to Fahrenheit\n2: Fahrenheit to Celsius")
    choice = int(input())
conv = Utility2.temp_conv(choice, temp)


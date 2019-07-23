# *********************************************************************************************
# Purpose: Program to convert a decimal No. to Binary.
# Author:  Damodhar D. Nirgude.
#  ************************************************************************************************
from Week1_Algo.Utility2 import Utility2
try:
    no = int(input("Enter a no. to convert it into a Binary format"))
except ValueError as e:
    print(e)
else:
    Utility2.to_binary(no)

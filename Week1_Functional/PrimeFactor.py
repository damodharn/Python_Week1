# *********************************************************************************************
# Purpose: Program to Compute the prime factorization of a given No.
# Author: Damodhar D. Nirgude.
#  ************************************************************************************************
from Week1_Functional.Utility import Utility
try:
    no = int(input("Enter that No. of which u wanted to find prime factors"))   # Taking i/p from user
except ValueError as e:
    print(e)
else:
    print("Prime Factors are: ")
    Utility.primefactor(no)  # Calling primefactor method from Utility class to calculate prime factors of the No.

# *********************************************************************************************
# Purpose: Program to Compute the prime factorization of a given No.
# Author: Damodhar D. Nirgude.
# Version: 3.1
#  ************************************************************************************************
from Week1_Functional.Utility import Utility
no = int(input("Enter that No. of which u wanted to find prime factors"))   # Taking i/p from user
print("Prime Factors are: ")
Utility.primefactor(no)  # Calling primefactor function from Utility class to calculate prime factors of the No.


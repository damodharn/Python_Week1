# *********************************************************************************************
# Purpose: Program to take a command-line argument N and prints a table of the
#           powers of 2 that are less than or equal to 2^N.
# Author: Damodhar D. Nirgude.
#  ************************************************************************************************
from Week1_Functional.Utility import Utility
import sys
try:
    no = int(sys.argv[1])  # Taking command line argument and storing it in integer format.
except ValueError as e:
    print("U've given Wrong i/p \n", e)
else:
    Utility.power(no)

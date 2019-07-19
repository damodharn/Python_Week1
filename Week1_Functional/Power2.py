# *********************************************************************************************
# Purpose: Program to take a command-line argument N and prints a table of the
#           powers of 2 that are less than or equal to 2^N.
# Author: Damodhar D. Nirgude.
# Version: 3.1
#  ************************************************************************************************
from Week1_Functional.Utility import Utility
import sys
no = int(sys.argv[1])
Utility.power(no)

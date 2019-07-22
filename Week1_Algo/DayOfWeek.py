# *********************************************************************************************
# Purpose: To write a program that takes a date as an input and
#           prints the day of the week that date falls on.
# Author:  Damodhar D. Nirgude.
#  ************************************************************************************************
from Week1_Algo.Utility2 import Utility2
import sys
print("U've Entered a Date: ")
d = int(sys.argv[1])
m = int(sys.argv[2])
y = int(sys.argv[3])
print("The Day on the Date:", d, "/", m, "/", y)
Utility2.day_of_week(d, m, y)

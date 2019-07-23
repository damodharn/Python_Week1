# *********************************************************************************************
# Purpose: To print the Euclidean distance from the point (x, y) to the origin (0, 0).
# Author:  Damodhar D. Nirgude.
#  ************************************************************************************************
from Week1_Functional.Utility import Utility
import sys
no1 = int(sys.argv[1])  # Converting command line argument1 to int and storing it.
no2 = int(sys.argv[2])  # Converting command line argument2 to int and storing it.
dist = Utility.distance(no1, no2)  # Calling distance function from Utility Class.
print("Euclidean distance of a given points from Origin(0,0)= ", dist)

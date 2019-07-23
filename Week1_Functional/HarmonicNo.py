# *********************************************************************************************
# Purpose: To Print the Nth harmonic number.
# Author:  Damodhar D. Nirgude.
#  ************************************************************************************************
from Week1_Functional.Utility import Utility
no = 0
while no == 0:  # Checking if Input entered by the user is Non-Zero or not.
    no = int(input("Enter a no.(greater than 0 or less than 0) to find Harmonic value "))
Utility.harmonicvalue(no)

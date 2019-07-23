# *********************************************************************************************
# Purpose: To Find the User Entered Year is Leap Year or not and then printing it.
# Author: Damodhar D. Nirgude.
#  ************************************************************************************************
from Week1_Functional.Utility import Utility

while 1:
    try:
        yr = int(input("Enter a year U want to check"))  # Accepting Year from User
    except ValueError as e:
        print(e)
    else:
        if yr < 1000 or yr > 9999:   # Checking weather user entered year is 4 digit no. or not
            print("Year must be a 4 digit No.")
        else:
            leap = Utility.leap_year(yr)  # Calling leap_year function from Utility class.
            break
if leap == 1:
    print(yr, "is a Leap Year")
else:
    print(yr, "is Not a Leap Year")

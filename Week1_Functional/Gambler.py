# *********************************************************************************************
# Purpose: To Simulates a gambler's program who start with $stake and place fair $1 bets until
#               he/she goes broke (i.e. has no money) or reach $goal.
# Author:  Damodhar D. Nirgude.
# Version: 3.1
#  ************************************************************************************************
from Week1_Functional.Utility import Utility

stake = int(input("Enter stake Value you wanted to add "))  # getting stake value from User.
goal = int(input("Enter a goal value u wanted to achieve "))     # getting goal value from User.
Utility.gamble(stake, goal)  # calling gamble method from Utility class.

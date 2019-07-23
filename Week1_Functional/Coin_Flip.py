# *********************************************************************************************
# Purpose: To Flip Coin and print percentage of Heads and Tails.
# Author: Damodhar D. Nirgude.
#  ************************************************************************************************
from Week1_Functional import Utility
no = int(input("Enter a No. of time u want to flip a coin"))  # Taking input from User.
heads = Utility.coin(no)  # Calling Function Coin to flip the coin.
tails = no - heads
print("u've played it for", no,  "times")  # no = total no. of times coin is flipped.
print("Heads= ", heads, "Tails= ", tails)
print("ur % of getting Heads is ", heads*100/no, "%", "and that of Tails is ", tails*100/no)

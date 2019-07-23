# *********************************************************************************************
# Purpose: Program to find  angram and paliandrome of prime No.
# Author:  Damodhar D. Nirgude.
#  ************************************************************************************************
from Week1_Algo.Utility2 import Utility2
print("Prime_Anagram_Numbers 0 to 1000")
try:
    no = int(input("enter last number:"))  # Upto which o/p will be shown
except ValueError as e:
    print("Plz Enter only integer\n", e)
else:
    Utility2.primeAanagram(no)

# *********************************************************************************************
# Purpose: Program to find a No. User thinks.
# Author:  Damodhar D. Nirgude.
#  ********************************************************************************************
import sys
from Week1_Algo.Utility2 import Utility2

no = int(sys.argv[1])

print("Think No. between 0 to", no-1, "I'll guess ur No. asking less than")
input("press any key after thinking")
Utility2.guess_no(no-1)


from Week1_Functional.Utility import Utility

while 1:
    yr = int(input("Enter a year U want to check"))
    if yr < 1000 or yr > 9999:
        print("Year must be a 4 digit No.")
    else:
        leap = Utility.leap_year(yr)
        break
if leap == 1:
    print(yr, "is a Leap Year")
else:
    print(yr, "is Not a Leap Year")

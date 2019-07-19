from Week1_Functional.Utility import Utility
import sys
no1 = int(sys.argv[1])
no2 = int(sys.argv[2])
dist = Utility.distance(no1, no2)
print("Euclidean distance of a given points from Origin(0,0)= ", dist)

# *********************************************************************************************
# Purpose: Program for measuring the time that elapses between
#            the start and end clicks.
# Author: Damodhar D. Nirgude.
# Version: 3.1
#  ************************************************************************************************
import time

print("Enter to start Stopwatch")
input()  # Take i/p from User to Start the Stop watch.
startTime = time.time()
print("Enter to Stop Stopwatch")
input()  # Take i/p from User to Stop the Stop watch.
stopTime = time.time()
sec = int(stopTime - startTime)  # Calculate elapsed time between start and stop in Sec.
if sec < 60:  # Checking if elapsed time is greater than a minute
    print(sec, 'sec')
else:
    mint = int(sec/60)  # Calculating No. of Minutes
    sec = sec % 60  # Calculating remaining Sec
    print(mint, 'min', sec, 'sec')

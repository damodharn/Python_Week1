import time

print("Enter to start Stopwatch")
input()
startTime = time.time()
print("Enter to Stop Stopwatch")
input()
stopTime = time.time()
sec = int(stopTime - startTime)
if sec < 60:
    print(sec, 'sec')
else:
    mint = int(sec/60)
    sec = sec % 60
    print(mint, 'min', sec, 'sec')

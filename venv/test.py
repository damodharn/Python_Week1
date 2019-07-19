import random
heads = 0
tails = 0
no = int(input("Enter the No. of times u wanted to flip the coin: "))
for x in range(no):
    if random.randint(0, 1) == 1:
        heads += 1
    else:
        tails += 1
print("u've played it for", no,  "times")
print("Heads= ", heads, "Tails= ", tails)
print("ur % of getting Heads is ", heads*100/no, "%", "and that of Tails is ", tails*100/no)

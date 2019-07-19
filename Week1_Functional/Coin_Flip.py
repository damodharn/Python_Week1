from Week1_Functional import Utility
no = int(input("Enter a No. of time u want to flip a coin"))
heads = Utility.coin(no)
tails = no - heads
print("u've played it for", no,  "times")
print("Heads= ", heads, "Tails= ", tails)
print("ur % of getting Heads is ", heads*100/no, "%", "and that of Tails is ", tails*100/no)

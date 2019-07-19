import random
import math

class Utility:
    # ######################## Method for coin Flipping #########################
    @staticmethod
    def coin(no):
        heads = 0
        for x in range(no):
            if random.randint(0, 1) == 1:
                heads += 1
        return heads
    # ######################## Leap Year Finding ###############################
    @staticmethod
    def leap_year(yr):
        if yr % 100 == 0:
            if yr % 400 == 0:
                return 1
            else:
                return 0
        elif yr % 4 == 0:
            return 1
        else:
            return 0
    #   #####################               Gambler          #####################################  #
    @staticmethod
    def gamble(stake, goal):
            cnt = 0
            win = 0
            while stake != 0 and stake != goal:
                cnt += 1
                if random.randint(0, 1) == 1:
                    stake += 1
                    win += 1
                else:
                    stake -= 1
            if stake == 0:
                print('Ooo...U lost')
            else:
                print('Congo...u win')
            print("u've played ", cnt, "and u won ", win, "games")
            print("u're Winning % is", win*100/cnt)
            print("u're loss % is ", (cnt-win)*100/cnt)
        # #############   """        Prime Factor Finding of a given No.    """     ##############
    @staticmethod
    def primefactor(no):
        for i in range(2, no):
            prime = 1
            if no % i == 0:
                for j in range(2, i//2 + 1):
                    if i % j == 0:
                        prime = 0
                        break
                if prime == 1:
                    print(i, end=" ")
    #   """        *******  Power of 2  *****          """     #
    @staticmethod
    def power(no):
        if no >= 0 and no < 32:
            print("Powers of 2 are:")
            for i in range(no+1):
                print("2^", i, "=", 2 ** i)
        else:
            print("Invalid Input..Plz enter a no. upto 31")
    #  *******************************   Harmonic Value    *************************  ##
    @staticmethod
    def harmonicvalue(no):
        sum = 0
        for i in range(1, no+1):
            sum = sum + 1/i
        print(no, "th Harmonic value= ", sum)
    #  ***********************  Euclidean Distance Calculation    ***************   ###
    @staticmethod
    def distance(x, y):
        dist = math.sqrt(x*x + y*y)
        return dist
    #  *****************************
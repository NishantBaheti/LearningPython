
import math
import os
import random
import re
import sys
from itertools import combinations


def stockmax(prices):
    all_desc = True
    for i in range(len(prices)-1):
        if prices[i] < prices[i+1]:
            all_desc = False
    if all_desc:
        return 0
    else:
        combs = combinations(prices, 2)
        max_profits = 0
        temp_profit = 0
        curr_day = None
        for comb in combs:
            if comb[0] != curr_day:
                curr_day = comb[0]
                max_profits += temp_profit
                temp_profit = 0

            if comb[1] > comb[0]:
                profit = comb[1] - comb[0]
                if profit > temp_profit:
                    temp_profit = profit
        max_profits += temp_profit
        return max_profits


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        print(result)

# Sample Input

# 3
# 3
# 5 3 2
# 3
# 1 2 100
# 4
# 1 3 1 2

# Sample Output

# 0
# 197
# 3




# """tough to look and understand
# test=int(input())
# for i in range(test):
#     n=int(input())
#     a=list(map(int,input().split()))
#     c=0
#     i=len(a)-1
#     while(i>=0):
#         d=a[i]
#         l=i
#         p=0
#         while(a[i]<=d and i>=0):
#             p+=a[i]
#             i-=1
#         c+=(l-i)*a[l]-p
#         continue
#     print (c)
# """



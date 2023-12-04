""""
dp[0] = 0
dp[1] = 1  
dp[2] = 1  
dp[3] = 1  
                            dp[4] = 2   dp[3] + dp[2]

dp[5] = 2   dp[4] + dp[3]
                            dp[6] = 3  dp[5] + dp[3]

dp[7] = 4   dp[6] + dp[4]
                            dp[8] = 5   dp[7] + dp[4]

dp[9] = 7   dp[8] + dp[5]
                            dp[10] = 9     dp[9]+dp[5]
dp[11] = 12  dp[10]+ dp[6]
                            dp[12] = 16 = dp[11] +dp[6]
"""

def solution(n):
    dp = [0, 1, 1, 1] # 0, 1, 2, 3
    
    for i in range(4, n+1):
        #짝수
       dp.append(dp[i-2]+dp[i-3])
       

    print(dp[n])

import sys
input = sys.stdin.readline
n = int(input()) #횟수
for i in range(n):
    number = int(input())
    solution(number)

# n = 1 ->1
# n = 2 -> 11 00
# n = 3 -> 111 100 001
# n = 4 -> 1111 1100 1001 0011 0000
# n = 5 -> 11111 11100 11001 10011 00111 10000 00100 00001
#피보나치 

dp = [0, 1, 2] # 1번째 2번째
def solution(n):
    for i in range(3,  n+1):
        dp.append((dp[i-1]+dp[i-2])%15746)

    print(dp[n]) 
     
import sys
input = sys.stdin.readline
n = int(input())
solution(n)
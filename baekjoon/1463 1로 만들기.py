#X가 3으로 나누어 떨어지면, 3으로 나눈다.
#X가 2로 나누어 떨어지면, 2로 나눈다.
#1을 뺀다.

# 인덱스가 0~3이 들어올시 위에 조건에 맞춰 아래 값이 나옴
# dp[0]은 0, dp[1] = 0, dp[2] = 1, dp[3] = 1
dp = [0, 0, 1, 1]
def make_one(n):
    for i in range(4, n+1):
        dp.append(dp[i-1] +1)
        if i % 2 == 0:
            dp[i] = min(dp[i//2]+1, dp[i])
        if i % 3 == 0:
            dp[i] = min(dp[i//3]+1, dp[i])  
    
    #ex) i = 5 인경우에는 조건들이 다 미통과 
    print(dp[n]) 


n = int(input())

print(5//3)
make_one(n)
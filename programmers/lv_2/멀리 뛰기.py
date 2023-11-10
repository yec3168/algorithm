# 재귀 정답은 되는거 같은데 시간초과
temp = 0
def dfs(n, sum):
    global temp
    if sum > n:
        return 0
    elif sum == n:
        return 1
    else:
       temp = dfs(n, sum+1) + dfs(n, sum+2)
    return temp

def recursive_solution(n):
    result = dfs(n, 0)
    print(result)
    return result % 1234567


# 반복문으로 풀기 
"""
1칸 =1
[1]

2칸 =2
[1, 1], [2]

3칸 가는법
[1, 2], [2, 1], [1, 1, 1] = 3

4칸 가는법
[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]= 5

? 피보나치 수열
"""
def solution(n):
    if n <3:
        return n
    # 0칸, 1칸, 2칸 가는법
    dp =[0, 1, 2]

    for i in range(3, n+1):
        dp.append(dp[i-1]+dp[i-2])
    return dp[n] % 1234567

#print(recursive_solution(3))
print(solution(3))
# 1. k칸 앞으로 점프
# 2. (현재 온 거리 ) x 2 순간이동

# 건전지는 순간이동시 소모 x
#         점프시 소모 -> k만큼

# 점프는 최소화 -> 건전지 소모량 적게


#  1 <= n <= 10억
#  k= 1이상 자연수

# 재귀는 max_deep 초과 이렇게 풀면 안될듯
result_dfs = 0
def recursive(n, k, sum):
    global result
    if sum == n:
        result_dfs = min(result_dfs, k)
    elif sum > n:
        result_dfs = min(result_dfs, n)
    else:
        recursive(n, k+1, sum+1)
        if sum != 0:
            recursive(n, k, sum*2)
    
    return result_dfs

def solution(n):
    result = 0
    while n > 0:
        result += n % 2
        n = n//2

    return result



solution(5)
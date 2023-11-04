# 자연수 n이 주어질 때 n을 표현하는방시에는 여러가지가 있음
# 그 연속한 자연수들로 표현하는 방법을 구하라
"""
1 + 2 + 3 + 4 + 5 == 15
4 + 5 + 6 = 15
7+ 8 = 15
15 = 15
"""


def solution(n):
    tmp = n
    count = 0
    if n <= 1:
        return 1
    while tmp >= 0:
        sum = 0
        for i in range(tmp, 0, -1):
            sum += i
            if sum == n:
                tmp -= 1
                count +=1
                break
            elif sum > n:
                tmp -= 1
                break
            if i == 1 and sum < n:
                tmp = -1
                break  
    return count




print(solution(15))
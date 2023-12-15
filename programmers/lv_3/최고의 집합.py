#1. 각 원소의 합이 S가 되는 수의 집합
#2. 위 조건을 만족하면서 각 원소의 곱 이 최대가 되는 집합

def solution(n, s):
    if n > s:
        return [-1]
    
    result =[ (s//n)  for _ in range(n) ]

    temp = s - sum(result)

    for i in range(temp):
        result[-1-i] += 1

    return result   

    
    

print(solution(2, 9))
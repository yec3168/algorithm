

# h개의 논문
# 1 ,2, 3, 4, 5, 6 ... ,h
# 각각 h번 이상 인용되도록 하는 가장 큰 h
"""
ex) 9, 7, 6, 2, 1 
(가장큰것부터 가장 작은 순으로) 저자의 index는 3입니다. 
"""
# f = 각 출판물의 인용 횟수
# 1. 가장 큰 값에서 가장 낮은 값으로 정렬 (내림차순)
# 2. f가 해당위치(position)보다 크거나 같은 마지막 위치를 찾습니다.

"""
ex) 10, 8, 5, 4, 3

4번째 출판물은 4이다.
"""


def solution(citations):
    citations = sorted(citations, reverse=True)
    result = -1
    for num in range(len(citations)):
        if num >= citations[num]:
            result = max(result, num)
            break
        if num == len(citations)-1 and result == -1:
            result = num+1
            break
    return result
    
print(solution([3, 0, 6, 1, 5]))
print(solution([10, 8, 5, 4, 3]))
print(solution([4, 3, 3, 3, 0, 0, 0]))
print(solution([25, 8, 5, 3, 3]))
print(solution([3, 4] ))
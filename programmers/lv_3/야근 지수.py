#시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값입니다

import heapq
# 재귀로 풀면 시간 초과 
def solution(n, works):
    heap = []

    for i in works:
        heapq.heappush(heap, -i)

    if abs(sum(heap)) <= n:
        return 0
    else:
        for i in range(n):
            q = heapq.heappop(heap)+1
            heapq.heappush(heap, q)
            
        result =[]
        for i in range(len(heap)):
            result.append(pow(heapq.heappop(heap),2))
        return sum(result)


print(solution(4, [4, 3, 3]))
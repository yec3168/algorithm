# 모든 음식의 스코빌 지수를 K 이상
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    result = 0 
    while scoville[0] < K:
        if len(scoville) <= 1 and min(scoville) < K:
            result = -1
            break
        heapq.heappush(scoville, (heapq.heappop(scoville) + heapq.heappop(scoville)*2))
        result +=1

    return result

print(solution([1, 2, 3, 9, 10, 12],	7))

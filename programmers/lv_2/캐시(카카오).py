from collections import deque

#도시이름을 검색하면 맛집 게시물들을 데이터 베이스에서 읽어주는 서비스
# 캐시크기를 얼마를 해야 효율적인지 
# 실행시간 측정 프로그램을 작성.
    
# 캐시크기(cacheSize 정수)와 도시이름(cities) 배열입력
def solution(cacheSize, cities):
    # queue.size = cacheSize
    queue = deque()

    if cacheSize == 0:
        return 5*len(cities)
    time_result = 0

    for i in cities:
        c= i.lower()
        if len(queue) == 0:
            queue.append(c)
            time_result += 5
        else:
            if c in queue:
                time_result +=1
                queue.remove(c)
                queue.append(c)
            else:
                time_result +=5
                if len(queue) >= cacheSize:
                    queue.popleft()
                queue.append(c)
    return time_result



print(solution(3, 	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]));
print(solution(3, 	["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, 	["Jeju", "Pangyo", "NewYork", "newyork"]))
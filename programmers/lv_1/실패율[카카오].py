# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

def solution(N, stages):
    stages.sort()
    dic = {}
    temp = []
    count = 1
    
    for i in range(1,N+1):
        dic[str(i)] = stages.count(i)

    N = len(stages)
    while True:
        if count > len(dic):
            break
        if dic[str(count)] == 0:
            temp.append( [count, 0])
        else:
            temp.append([count, dic[str(count)]/N])
        N -=dic[str(count)]
        count +=1
    temp = sorted(temp, key = lambda x : x[1], reverse=True)
    result =[]
    for i in temp:
        result.append(i[0])

    return result
print(solution(5,	[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,	[4,4,4,4,4]))
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

def solution(N, stages):
    stages.sort()
    dic = {}
    
    for i in range(1,N+1):
        dic[str(i)] = stages.count(i)
    dic[str(N)]  += stages.count(N+1)

    


    
    


print(solution(5,	[2, 2, 2, 6, 2, 4, 3, 3]))
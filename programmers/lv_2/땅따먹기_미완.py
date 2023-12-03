#땅따먹기 게임에는 한 행씩 내려올 때, 
#같은 열을 연속해서 밟을 수 없는 특수 규칙이 있습니다.


# 나오긴 하는데 재귀 함수횟수 초과 시간 초과
import sys
sys.setrecursionlimit(10^10)
result = 0
def dfs(land ,cur_position, cur_sum, cur_depth):
    global result
    if cur_depth == len(land):
        return cur_sum
    else:
        for i in range(1, 4):
            result = max(result, dfs(land,(cur_position+i)%4,cur_sum+land[cur_depth][(cur_position+i)%4],cur_depth+1))
    return result
def solution2(land):
    
    return dfs(land, 0, 0, 0)



print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
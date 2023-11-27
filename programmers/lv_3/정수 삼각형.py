
def solution(triangle):
    if len(triangle) == 1:
        return triangle[0][0]
    #양 끝 더하기
    for i in range(1,len(triangle)):
        triangle[i][0] += triangle[i-1][0]
        triangle[i][-1] += triangle[i-1][-1]
    if len(triangle) > 2:
        for i in range(2, len(triangle)):
            for j in range(1, len(triangle[i])-1):
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    
    return max(triangle[-1])

#오류
result = 0
def dfs(triangle, cur_poisition, cur_sum, i):
    if cur_poisition >= len(triangle):
        return cur_sum
    elif i <= cur_poisition+1:
        result =  max(dfs(triangle, cur_poisition+1, cur_sum + triangle[cur_poisition][i], i), dfs(triangle, cur_poisition+1, cur_sum + triangle[cur_poisition][i], i+1))

    return result

def solution2(triangle):
    answer = dfs(triangle, 1, 7, 0) #오류
    return answer



print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
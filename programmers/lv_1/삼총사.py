# 3개의 정수의 합이 0일 경우 삼총사이다

"""
[-2, 3, 0, 2, -5]

-2 + 0 + 2 = 0

3 + 2 + -5 = 0
"""


def solution(number):
    result = 0

    for i in range(len(number)-2):
        for j in range(i+1, len(number)-1):
            for z in range(j+1, len(number)):
                if (number[i]+ number[j]+ number[z]) == 0:
                    result +=1

    
    return result


print(solution([-2, 3, 0, 2, -5]))


# 다른 사람 풀이



def sol2(number):

    result = 0
    
    # i현재 위치, cnt 갯수, sum_num 더한 값
    def dfs(i, cnt, sum_num):
        nonlocal result
        # 갯수가 3개이면서 sum_num =0 일때만 result 증가
        if cnt == 3 and sum_num == 0:
            result += 1
            return
        # i의 위치가 리스트의 끝일경우 중지
        if i ==len(number):
            return
        # 갯수가 3개이하일때만 두가지 경우로 dfs 실행
        # 리스트의 인덱스를 한개 증가시키고 cnt도 증가 기존의 값은 더함
        # 
        if cnt < 3:
            dfs(i +1 , cnt +1, sum_num + number[i])
            dfs(i +1 , cnt, sum_num)

    
    dfs(0, 0, 0)

    answer =result
    return answer


print(sol2([-2, 3, 0, 2, -5]))
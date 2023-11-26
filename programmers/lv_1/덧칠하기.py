#처음 칠할떄 빈 곳을 가장 많이 채울수 있는곳 
# 그다음도 계속 max값을 구해서 칠할 수 있는 곳이 가장 많은 순으로 

def solution(n, m, section):
   
    position = section[0]
    result =1

    for i in section:
        #print(position, i)
        if position + (m-1) < i:
            position = i
            result +=1

    return result

print(solution(8,	4,	[2, 3, 6]))

print(solution(4,	1,	[1, 2, 3, 4]))
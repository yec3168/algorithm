# k점이 최상품, 1이 최하품
# m개씩 포장 
# 가격은 가장 낮은 점수 p * m
# 남는 사과는 버림 (몫만 남기는 듯)

def solution(k, m, score):
    score = sorted(score, reverse=True)
    
    sell_box = len(score)// m # 팔수 있는 상자 개수.

    result_list = []

    for i in range(sell_box):
        result_list.append(score[m*i:(m*i)+m])

    result = 0
    for i in result_list:
        result += i[m-1]*m
    

    return result


print(solution(3,	4,	[1, 2, 3, 1, 2, 3, 1]))
print(solution(4,	3,	[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))
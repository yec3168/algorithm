def solution(k, tangerine):
    not_sorted = {}

    # 0으로 초기화
    for i in tangerine:
        not_sorted[str(i)] = 0
    # 값을 더함.
    for i in tangerine:
        not_sorted[str(i)] = not_sorted[str(i)]+1
    
    # 정렬
    sort_dict= dict(sorted(not_sorted.items(), key=lambda x:(x[1], x[0]), reverse=True))
    #print(sort_dict.items())

    sum = 0
    count = 0

    for key, value in sort_dict.items():
        k -=value
        count +=1
        if k <= 0:
            break
            
    
    return count


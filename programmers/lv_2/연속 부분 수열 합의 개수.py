def solution(elements):
    result = set(elements)
    #print(result)

    # 부분 집합 구하기
    subsets = [[]]
    for i in elements:
        size = len(subsets)
        print(size)
        for j in range(size):
            subsets.append(subsets[j]+[i])
    
    print(subsets)
    for i in subsets:
        result.add(sum(i))

    result.pop()
    return len(result)





print(solution([7,9,1,1,4]))
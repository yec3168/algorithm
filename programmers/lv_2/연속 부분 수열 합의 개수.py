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

# 다른사람풀이
def solution(elements):
    result = set()

    i = 0 
    while i < len(elements):
        i += 1
        for j in range(len(elements)):
            if i + j <= len(elements):
                # 0 : 0+1   0: 0+2  0 : 0+3     0 : 0+4
                # 1 : 1+1
                #print((elements[j : j+i]))
                result.add(sum(elements[j : j+i])) 
            else:
                result.add(sum(elements[j:])+sum(elements[:i+j-len(elements)]))
                

    return len(result)




print(solution([7,9,1,1,4]))
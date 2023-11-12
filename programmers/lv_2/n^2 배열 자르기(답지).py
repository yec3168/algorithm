def solution(n, left, right):

    # 1번쨰
    list_num = [ [0]*(n) for _ in range(n)]

    # 2번쨰  
    list_num[0][0] = 1
    for i in range(0, n):
        for j in range(0, i):
            list_num[i][j] = i+1
            list_num[j][i] = i+1
            list_num[i][i] = i+1
    
    # 2차원 리스트를 1차원 리스트로
    list_num2 = sum(list_num, [])
    
    print(list_num2)
    return list_num2[left:right+1]


## 답지 보고 풀음
def solution2(n, left, right):
    result = []
    for num in range(left, right+1):
        result.append( max(num//n, num % n)+1)
        
    return result

    
    

#print(solution(3, 2, 5))
#print(solution(4, 7, 14))

print(solution2(3, 2, 5))
print(solution2(5, 1, 5))
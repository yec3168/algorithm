# 시간 복잡도 O(루트n)
def solution(n):
    result = 0
    for i in range(2, n+1):
        find =True
        for j in range(2, int(i ** 0.5)+1):
            if i % j == 0:
                find = False
                break
        if find == True:
            print(i)
            result +=1

    return result


# 반복문 시간초과남 
def solution2(n):
    result = 0
    for i in range(2, n+1):
        find =True
        for j in range(2, (i-1)):
            if i % j == 0:
                find = False
                break
        if find == True:
            print(i)
            result +=1

    return result

print(solution(10))
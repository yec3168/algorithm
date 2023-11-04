def solution(x):
    result = False

    sum = 0
    temp =x
    while temp > 0:
        sum = sum + int(temp % 10)
        temp = int(temp / 10)
    
    
    if x % sum == 0:
        result = True

    print(sum)
    return result

print(solution(11))

# 다른 풀이

def solution2(n):
    sum = 0
    result = False
    for i in str(n):
        sum = sum + int(i)
    
    if n % sum == 0:
        result = True

    return result


print(solution2(12))
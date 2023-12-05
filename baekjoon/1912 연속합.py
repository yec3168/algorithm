# 답지
def solution(numbers):
    for i in range(1, len(numbers)):
        numbers[i] = max(numbers[i], numbers[i]+numbers[i-1])


    return max(numbers)


# 반복문은 시간 초과 
def solution2(numbers):
    dp =[]
    result = numbers[0]
    for i in range(len(numbers)):
        sum = numbers[i]
        for j in range(i+1, len(numbers)):
            sum += numbers[j]
            result = max(result, sum)

    
    return result


import sys
input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().split()))
    
print(solution(numbers))


def solution(numbers):
    temp = [ -1 for _ in range(len(numbers))]
    stack =[]
    for n in range(len(numbers)):

        # stack이 비어있거나 number[마지막에 넣은 위치] 가 현재 위치보다 크면
        # temp에 갱신
        while stack and numbers[stack[-1]] < numbers[n]: 
            temp[stack.pop(-1)] = numbers[n]
        
        stack.append(n)

    
    return temp

# 시간초과
def solution2(numbers):
    result = []

    for n in range(len(numbers)-1):
        find = False
        for i in range(n+1, len(numbers)):
            if numbers[n] < numbers[i]:
                find = True
                result.append(numbers[i])
                break
        if find == False:
            result.append(-1)
    #마지막
    result.append(-1)


    return result

# 시간초과
def solution3(numbers):
    result = []

    for n in range(len(numbers)-1):
        find = False
        temp = sorted(numbers[n+1:],reverse=True)
        if temp[0] <= numbers[n]:
            result.append(-1)
            continue
        for i in range(n+1, len(numbers)):
            if numbers[n] < numbers[i]:
                result.append(numbers[i])
                break
    
    #마지막
    result.append(-1)

    return result


print(solution([9, 1, 5, 3, 6, 2]))
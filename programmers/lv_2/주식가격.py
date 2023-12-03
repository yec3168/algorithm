def solution(prices):
    result =[]

    for i in range(len(prices)):
        count = 0
        find = True
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                find = False
                result.append(count+1)
                break
            else:
                count+=1
        if find == True:
            result.append(count)

    return result

print(solution([1, 2, 3, 2, 3]))
print(solution([4, 5, 1, 2, 6, 1, 1]))
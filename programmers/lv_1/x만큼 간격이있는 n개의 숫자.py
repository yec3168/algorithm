def solution(x, n):
    list =[]
    for i in range(1, n+1):
        list.append(i*x)

    return list


print(solution(0, 5))
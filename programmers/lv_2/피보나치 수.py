def solution(n):

    list = [0, 1] # 0번쨰 1번째

    for i in range(2,n+1):
        list.append(list[i-1]+list[i-2])

    print(list)

    return list[n] % 1234567

print(solution(3))
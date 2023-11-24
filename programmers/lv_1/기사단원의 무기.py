# https://kbw1101.tistory.com/32 해당 알고리즘 참고
def solution(number, limit, power):
    result_list = []
    for i in range(1, number+1):
        count = 0
        find = True
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                count +=1
                if j != (i/j):
                    count +=1
            if count > limit:
                result_list.append(power)
                find = False
                break
        if find == True:
            result_list.append(count)
    #print(result_list)
    return sum(result_list)



# 반복문 시간초과
def solution2(number, limit, power):
    result_list = []
    for i in range(1, number+1):
        count = 0
        find = True
        for j in range(1, i+1):
            if i % j == 0:
                count +=1
            if count > limit:
                result_list.append(power)
                find = False
                break
        if find == True:
            result_list.append(count)

    return sum(result_list)
print(solution(5, 3, 2))
print(solution(10, 3, 2))

print(solution2(5, 3, 2))
print(solution2(10, 3, 2))
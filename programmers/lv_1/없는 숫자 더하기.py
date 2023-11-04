def solution(numbers):
    result = 0
    for i in range(10):
        if i not in numbers:
            result = result + i

    return result
#sum(i if i in numbers for i in range(9))


list = [1,2,3,4,6,7,8,0]
print(solution(list))


#다른 사람 풀이
def sol2(numbers):
    return 45 - sum(numbers)

print(sol2(list))
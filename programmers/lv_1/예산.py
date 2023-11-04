def solution(d, budget):
    d.sort()
    sum = 0
    count = 0
    if d[0] > budget:
        return 0
    elif d[0] == budget:
        return 1
    
    for i in d:
        if sum > budget:
            count -= 1
            break
        elif sum == budget:
            break
        else:
            count += 1
        sum += i
    return count


print(solution([2,2,3,3],	10))



# 다른 사람 풀이

def sol2(d, budget):
    d.sort()

    while budget < sum(d):
        d.pop()
    
    return len(d)

print(sol2([2,2,3,3],	10))
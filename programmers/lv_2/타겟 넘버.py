result = 0
def dfs_recursive(numbers, target, cnt, sum):
    global result
    if cnt == len(numbers):
        if sum == target:
            return 1
        else:
            return 0
    else:
        result = dfs_recursive(numbers, target, cnt+1, sum + numbers[cnt]) + dfs_recursive(numbers, target, cnt+1, sum - numbers[cnt]) 
    return result
        


def solution(numbers, target):
    result = dfs_recursive(numbers, target, 0, 0)
    return result 


print(solution([1, 1, 1, 1, 1],	3))
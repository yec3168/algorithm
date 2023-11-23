# nums 숫자 중 3개를 선택하여 더한 값이 소수가 되는 경우의 수를 return

from itertools  import combinations

def solution(nums):
    
    list_a = list(combinations(nums, 3))
    result = 0
    for i in list_a:
        sum_i = sum(i)
        found = True
        for i in range(2,sum_i-1):
            if sum_i % i == 0:
                found = False
                break
        
        if found == True:
            result +=1
        
    return result

print(solution([1,2,3,4]))
# N 마리의 폰켓몬 중에서 N/2마리를 가져가도 좋다
# 같은 종류의 폰켓몬은 같은 번호를 가지고 있다

# ex)
"""
[3번, 1번, 2번, 3번]
첫 번째(3번), 두 번째(1번) 폰켓몬을 선택
첫 번째(3번), 세 번째(2번) 폰켓몬을 선택
첫 번째(3번), 네 번째(3번) 폰켓몬을 선택
두 번째(1번), 세 번째(2번) 폰켓몬을 선택
두 번째(1번), 네 번째(3번) 폰켓몬을 선택
세 번째(2번), 네 번째(3번) 폰켓몬을 선택

중 3번, 3번을 고르는거 말고 서로 다른 종류를 고르는 최대값 2
"""
# 최대한 다양한 종류의 폰켓몬을 가진다.

from itertools import combinations, permutations

def solution(nums):
    choice = len(nums)//2 # 가져가야할 포켓몬의 수
    set_nums = len(set(nums)) # 포켓몬이 총 몇마리인지

    result = min(choice, set_nums)
    return result


# 조합으로 풀시 시간초과
def solution2(nums):
    choice = len(nums)//2
    result = 0
    # 조합 구하기
    perm = list(combinations(nums, choice))
    print (perm)

    for i in perm:
        set_perm = set(i)
        result = max(result, len(set_perm))


    # for i in range(0, len(nums)-(choice+1)):
    #     result_set = set()
    #     for j in range(i, i+choice):
    #         resul_set.add(nums[j])
    #     result = max(result, len(result_set))        
    

    return result

print(solution([3,3,3,2,2,4]))
print(solution([3,1,2,3]))


print(solution2([3,1,2,3]))
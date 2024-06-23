#알아볼 수 없는 번호를 0

from collections import defaultdict

def solution(lottos, win_nums):
    dic = defaultdict(int)
    count = 1
    for i in range(6, -1, -1):
        dic[str(i)] = count
        if count <6:
            count +=1
    min = 0
    zero_count = 0
    for i in range(len(lottos)):
        if lottos[i] == 0:
            zero_count +=1
        if lottos[i] in win_nums:
            min +=1

    max = min + zero_count
    return [dic[str(max)], dic[str(min)]]

print(solution([44, 1, 0, 0, 31, 25],	[31, 10, 45, 1, 6, 19]))

print(solution([7,8,9,10,11,12], [1, 2, 3, 4, 5, 6]))
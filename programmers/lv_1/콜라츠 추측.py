# 입력된 수가 짝수라면 2로 나눕니다.
# 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
# 결과로 나온 수에 가은 작업을 하여 1이 될 때 까지 반복합니다.

"""
 n = 6
 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
"""

def solution(num):
    count = 0

    while True:
        if count >=500:
            return -1
        if num == 1:
            break


        if num % 2 == 0:
            num = num / 2
            count = count + 1
        else:
            num = (num * 3) + 1
            count = count +1

    return count


print(solution(626331))


# 다른 사람 풀이

def loop_solutuon(num):

    for i in range(500):
        num = num / 2 if num % 2 == 0 else num * 3+1
        if num == 1:
            return i+1
    
    return -1

print(loop_solutuon(8))
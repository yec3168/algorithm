# 10진수 -> 3진수 -> 리버스 3진수 -> 10진수
"""
45 -> 1200 -> 0021 -> 7
"""
import string

tmp = string.digits+string.ascii_lowercase

def convert(num , base):
    q, r = divmod(num, base)
    if q==0:
        return tmp[r]
    else:
        return convert(q, base)+tmp[r]

def reverse(num):
    return num[::-1]


def solution(n):
    return int(reverse(convert(n, 3)),3)


print(solution(45))




# 다른 사람 풀이
# // = 나누는데 결과를 정수로 표현.
def sol2(n):
    tmp =""
    
    while n:
        tmp = tmp + str(n % 3)
        n = n//3 
    
    result = int(tmp, 3)
    return result

print(sol2(45))
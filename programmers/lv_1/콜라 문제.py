# a를 가져가면 b를 줌
# n= 가지고있는 빈 콜라 개수

def solution(a, b, n):
    drink_cola = 0
    while n >=a:
       drink_cola += (n//a)*b
       n = ((n//a)*b)+(n%a)

    return drink_cola


print(solution(3, 1, 20))
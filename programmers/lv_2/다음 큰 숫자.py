# 자연수 n이 주어졌을 때, 조건에 맞춰 다음 큰 숫자를 정의한다.

# 조건1. n의 다음 큰 숫자는 n보다 큰 자연수
# 조건2. n의 다음 큰 숫자와 n은 2진수롸 변환 했을때 1의 숫자가 같아야한다.
# 조건3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 숫자여야한다.

"""
78 ( 1001110 ) 1의숫자 4

83( 1010011 ) 1의 숫자 4

"""
def one_number(n):
    count = 0
    for i in str(n):
        if i == "1":
            count +=1
    return count 

def solution(n):
    tmp = one_number(bin(n))
    #print(tmp)
    while True:
        n = n + 1
        if tmp == one_number(bin(n)):
            result = n
            break

    return result

print(solution(78))
import sys
input = sys.stdin.readline


def solution(num):
    s = sorted(list(str(num)), reverse=True)
    print(''.join(s))

num = int(input()[:-1])
solution(num)
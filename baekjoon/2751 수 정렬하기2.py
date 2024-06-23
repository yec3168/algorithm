import sys
input=sys.stdin.readline
def solution(list_num):
    for i in sorted(list_num):
        print(i)

n = int(input())
list_num = []
for i in range(n):
    list_num.append(int(input()))

solution(list_num)

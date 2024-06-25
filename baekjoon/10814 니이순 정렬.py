import sys
input = sys.stdin.readline


def solution(user_list):
    for i in sorted(user_list, key=lambda x : x[0]):
        print(i[0], i[1])
    

n = int(input())
user_list = []

for i in range(n):
    age, name = input().split()
    user_list.append([int(age), name])

solution(user_list)
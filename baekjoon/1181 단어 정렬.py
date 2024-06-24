import sys
input = sys.stdin.readline

def find_keys(dict, val):
  return list(key for key, value in dict.items() if value == val)

def solution(strings):
    sorted_key = sorted(strings.items(), key = lambda item : item[1])
    answer= [];
    for i in range(int(sorted_key[-1][1])+1):
        keys = find_keys(strings, i)
        if len(keys) == 0 :
            continue
        for j in sorted(keys):
            answer.append(j)
    
    
    for i in answer:
        print(i)

        



n = int(input())
strings = dict()

for i in range(n):
    s = input()[:-1]
    strings[s] = len(s)

print()
solution(strings)
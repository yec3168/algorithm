#1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
#2. words에 있는 단어로만 변환할 수 있습니다.

from collections import deque

def bfs(begin, target, words):
    temp =[begin, 0]
    queue = deque([temp])
    print(queue)

    result = 0
    while queue:
        q = queue.popleft()
        for word in words:
            count = 0
            for i in range(len(word)):
                if word[i] != q[0][i]:
                    count +=1
            # 각각의 단어가 차이가 1개만 났을 때 넣음.
            if count == 1:
                if word == target:
                    return q[1]+1
                queue.append([word, q[1]+1])

def solution(begin, target, words):
    if target not in words:
        return 0
    
    return  bfs(begin, target, words)
        



print(solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"]))
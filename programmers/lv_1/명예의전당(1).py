from collections import deque


def solution(k, score):
    queue = deque()

    # 맨 처음은 queue에 넣음queue.append()
    result = []
        
    
    for i in range(len(score)):
        if len(queue) != 0:
            result.append(queue[len(queue)-1])

        if len(queue) == k:
            if queue[k-1] < score[i]:
                queue.pop()
            else:
                continue
        queue.append(score[i])
        queue = deque(sorted(queue, reverse=True))
    
    result.append(queue[len(queue)-1])
    return result


print(solution(3,	[10, 100, 20, 150, 1, 100, 200]))

print(solution(4, 	[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))
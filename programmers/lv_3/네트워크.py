from collections import deque

def solution(n, computers):
    visited = [ False for _ in range(n)]
    result = 0
    count = 0
    while True:
        if False not in visited:
            break;
        queue = deque()
        if visited[count] == True:
            count +=1
            continue
        else:
            queue.append(count)
            visited[count] = True
            result +=1
            count +=1
        while queue:
            q = queue.popleft()
            for i in range(len(computers[q])):
                if computers[q][i] == 1 and visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    return result
    

print(solution(3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print()
print(solution(3,	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

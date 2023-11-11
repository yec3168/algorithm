from collections import deque

def bfs(maps, n, m):
    queue = deque()

    queue.append((0, 0))

    dx = [0, 1 ,0 ,-1] # 오, 아, 왼, 위
    dy = [1, 0, -1, 0]
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위안에 든다면
            if 0 <= nx and nx < n and 0 <= ny and ny < m:
                if maps[nx][ny] == 1: # 벽이 아니면서 처음 방문
                    queue.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1
    
    if maps[n-1][m-1] == 1:
        return -1
    else: 
        return maps[n-1][m-1] 
    

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    result = bfs(maps, n, m)
    return result


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))

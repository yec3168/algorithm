#dfs로 풀며 (0, 0)에서 (n,m)로 가는데 아래 오른쪽만 보면 될 듯?

from collections import deque

dx = [1, 0, -1, 0] #아래 오른쪽 위 왼쪽
dy = [0, 1, 0, -1]

def bfs(maps, start_x, start_y, n, m):
    visited = [[False]*m for _ in range(n)]

    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = True

    #print(queue)
    #print(visited)

    # queue가 빌 때까지
    while queue:
        start_x, start_y = queue.popleft()
        for i in range(4):
            now_x = start_x + dx[i]
            now_y = start_y + dy[i]
            if now_x >=0 and now_x < n and now_y >= 0 and now_y < m:
                #방문한적 없으면
                if maps[now_x][now_y] == 1:
                    if visited[now_x][now_y] == False:
                        queue.append((now_x, now_y))
                        visited[now_x][now_y] = True
                        maps[now_x][now_y] = maps[start_x][start_y] + 1
    if maps[n-1][m-1] == 1:
        return -1
    
    return maps[n-1][m-1]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    if maps[n-2][m-1] == 0 and maps[n-1][m-2] ==0:
        return -1
    
    result = bfs(maps, 0, 0, n, m)
    return result


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
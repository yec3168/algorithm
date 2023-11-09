# 방문할 수 있는 정점이 여러 개인 경우 정점번호가 작은 것 먼저
# 더 이상 방문 할 점이 없을 경우 종료

# n = 정점 수, m = 간선의 수 , v = 시작할 번호


import sys
sys.setrecursionlimit(10**6)
n, m, v = map(int, sys.stdin.readline().split())

#https://duwjdtn11.tistory.com/515 참고
# 4 * 4 만듬
adj = [ [] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    adj[x].append(y)
    adj[y].append(x)

sort_adj = []
for i in adj:
    i.sort()
    sort_adj.append(i)

# dfs 재귀함수
visited_dfs =[]
def dfs_recursive(sort_adj, cur_position):

    # 만약 방문했으면 돌아감
    if cur_position in visited_dfs:
        return
    
    # v먼저 추가
    visited_dfs.append(cur_position)
    print(cur_position, end =" ")
    for node in sort_adj[cur_position]:
        dfs_recursive(sort_adj, node)

dfs_recursive(sort_adj, v)
print()


from collections import deque

visited_bfs = [False]*(n+1)

def bfs(sort_adj, start, visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end =" ")

        for i in sort_adj[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
    return 0

bfs(sort_adj, v, visited_bfs)
from collections import deque

n, m, k, x = map(int, input().split()) # 도시 수, 도로 수, 거리 정보, 출발 도시 번호
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) #인접리스트 형태로...(도로 말고 도시 기준)

dist = [-1]*(n+1) # -1이면 미방문, 도시 번호 1부터 시작이라 n+1 크기로 초기화

def bfs(x):

    queue = deque()
    queue.append(x)
    
    dist[x] = 0
    
    while queue:
        
        v = queue.popleft()
        for i in graph[v]:
            if dist[i] == -1:
                dist[i] = dist[v] + 1
                queue.append(i)
                
    return False

bfs(x)

cnt = 0

for i in range(1, n+1):
    if dist[i] == k:
        print(i)
        cnt += 1
    
if cnt == 0:
    print(-1)
n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)] # 공백 없이 입력이면 split x

def dfs(x, y):
    # 주어진 범위 벗어나면 종료
    if x<0 or x>=n or y<0 or y>=m: 
        return False
    
    # 현재 노드가 아직 방문 전일 때
    if graph[x][y] == 0:
        # 방문 처리
        graph[x][y] = 1
        # 상하좌우 위치 모두 재귀적 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        
        return True
    return False

ice_cnt = 0

for i in range(n):
    for j in range(m):
        # 현재 위치에서 dfs 수행
        if dfs(i, j) == True:
            ice_cnt += 1
            
print(ice_cnt)

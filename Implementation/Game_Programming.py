n, m = map(int, input().split()) # 맵 크기 N*M
a, b, d = map(int, input().split()) # 현재 캐릭터 좌표(a,b), 바라보고 있는 방향 d(0 북 1 동 2 남 3 서)
map = [list(map(int, input().split())) for _ in range(n)] # 바다 1, 육지 0

# 순서대로 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1
turn_time = 0

visited = [[0]* m for _ in range(n)]
visited[a][b] = 1


def turn_left():
    global d
    if d == 0: 
        d = 3
    else:
        d -= 1
    

while True:
    turn_left()
        
    nexta= a + dx[d]
    nextb= b + dy[d]
            
    if map[nexta][nextb] == 0 and visited[nexta][nextb] == 0:
        a, b = nexta, nextb
        visited[a][b] = 1
        count +=1
        turn_time = 0
        continue
    else:
        turn_time += 1
        
    if turn_time == 4:
        nexta= a - dx[d]
        nextb= b - dy[d]
        if map[nexta][nextb] == 0:
            a, b = nexta, nextb
            turn_time = 0    
        else:
            break

print(count)
                
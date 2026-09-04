n,m = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(n)]
mins = []
for row in cards:
    mins.append(min(row))
    
print(max(mins))
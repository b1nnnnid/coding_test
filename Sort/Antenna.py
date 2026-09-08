n = int(input()) #집 수
locations = sorted(list(map(int, input().split())))

print(locations[(n - 1) // 2])

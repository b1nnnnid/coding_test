n = int(input())
coins = sorted(list(map(int, input().split())))

target =1
for c in coins:
    if target < c:
        break
    else:
        target += c
        
print(target)
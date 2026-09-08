n, k = map(int, input().split()) # 배열 크기, 바꿔치기 연산 가능 횟수
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
    
print(sum(a))
    



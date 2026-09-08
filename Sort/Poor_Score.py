n = int(input())
scores = [list(input().split()) for _ in range(n)]

scores = sorted(scores, key = lambda student: student[1])

for s in scores:
    print(s[0], end=" ")

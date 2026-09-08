# 국영수

n = int(input()) # 학생 수
scores = [list(input().split()) for _ in range(n)] # [이름, 국어점수, 영어점수, 수학점수]

# 괄호로 묶어서 정렬 가능
sorted = sorted(scores, key = lambda s: (-int(s[1]), int(s[2]), -int(s[3]), s[0]))

for s in sorted:
    print(s[0])
n,m,k = map(int,input().split()) #배열크기 n, 숫자가 더해질 횟수 m, 특정 인덱스를 연속으로 더할 수 있는 횟수 k
arr = sorted(list(map(int, input().split())), reverse=True)

# 수열로 풀어보기(반복문 말고)

a,b = arr[0], arr[1]
countA = m//(k+1)*k #한바퀴(k번 더하고 한 번 다른 거)로 나눠서 큰 수 더해질 횟수
countA += m%(k+1) # 나머지만큼 더 더하기 

sum = a*countA + b*(m-countA)
print(sum)
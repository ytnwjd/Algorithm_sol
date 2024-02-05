import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
numbers = [0]
cnt = 0

for i in range(n):
    numbers.append(num[i] + numbers[i]) # prefix alo 사용

for i in range(n+1):
    for j in range(1, n+1):
        # print("!!", numbers[j] - numbers[i])
        if (numbers[j] - numbers[i] == m):    
            cnt += 1

print(cnt)   
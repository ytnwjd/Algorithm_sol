import sys as sys
n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
p = [0]
for i in range(n):
    p.append(num[i]+p[i])
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(p[j]-p[i-1])
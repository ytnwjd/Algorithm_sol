import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = []
for i in range(1, n+1):
    ans = n % i
    if (ans == 0):
        li.append(i)

if (len(li) < k):
    print(0)
else:
    print(li[k-1])
n, m = map(int, input().split())
tmp = 0
array = [0]*n
for ball in range(n):
    array[ball] = ball+1
for _ in range(m):
    i, j = map(int, input().split())
    tmp = array[i-1]
    array[i-1] = array[j-1]
    array[j-1] = tmp
for ball in range(n):
    print(array[ball], end=' ')
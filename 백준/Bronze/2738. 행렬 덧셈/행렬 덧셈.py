n, m = map(int, input().split())
A = [] ;   B = [] ;  sum = []
for i in range(n):
    A.append([])
    B.append([])
    sum.append([])
    for _ in range(m):
        A[i].append(0)
        B[i].append(0)
        sum[i].append(0)
for i in range(n):
    num = list(map(int, input().split()))
    for j in range(m):
        A[i][j] = num[j]
for i in range(n):
    num = list(map(int, input().split()))
    for j in range(m):
        B[i][j] = num[j]
for i in range(n):
    for j in range(m):
        sum[i][j] = (A[i][j] + B[i][j])
for i in range(n):
    for j in range(m):
        print(sum[i][j], end=" ")
    print()
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
# print(x)
# print(y)
coor = [[0] * 202 for _ in range(202)]
OFFSET = 100

for i in range(n):
    for xi in range(y[i], y[i]+8):
        for yi in range(x[i], x[i]+8):
            # print(y[i], x[i])
            coor[OFFSET+xi][OFFSET-yi] = 1

tot =0
for i in range(202):
    for j in range(202):
        if coor[i][j] == 1:
            tot += 1

print(tot)
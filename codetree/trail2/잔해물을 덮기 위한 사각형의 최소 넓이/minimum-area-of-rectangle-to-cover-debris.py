x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
coor = [[0] * 2002 for _ in range(2002)]
OFFSET = 1000

for i in range(y1[0], y2[0]):
    for j in range(x1[0], x2[0]):
        coor[OFFSET+i][OFFSET-j] = 1


for i in range(y1[1], y2[1]):
    for j in range(x1[1], x2[1]):
        if coor[OFFSET+i][OFFSET-j] == 1:
            coor[OFFSET+i][OFFSET-j] -= 1

min_x1 = float("INF")
max_x2 = float("-INF")
min_y1 = float("INF")
max_y2 = float("-INF")
has_remain = False

for i in range(2002):
    for j in range(2002):
        if coor[i][j] == 1:
            has_remain = True

            min_x1 = min(j, min_x1)
            max_x2 = max(j + 1, max_x2)  # 오른쪽 끝 좌표는 + 1
            min_y1 = min(i, min_y1)
            max_y2 = max(i + 1, max_y2)  # 위쪽 끝 좌표는 + 1
            
if has_remain:
    print((max_x2 - min_x1) * (max_y2 - min_y1))
else:
    print(0)
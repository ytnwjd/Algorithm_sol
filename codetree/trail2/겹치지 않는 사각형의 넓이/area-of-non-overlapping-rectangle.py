x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())  # A
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())  # B
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())  # M


# Please write your code here.
coor = [[0] * 2002 for _ in range(2002)]
OFFSET = 1000

# a와 b 사각형에 1 표시
for st in range(2):
    for i in range(y1[st], y2[st]):
        for j in range(x1[st], x2[st]):
            coor[OFFSET + i][OFFSET - j] = 1

for i in range(y1[2], y2[2]):
    for j in range(x1[2], x2[2]):
        if coor[OFFSET + i][OFFSET - j] == 1:
            coor[OFFSET + i][OFFSET - j] -= 1

tot = 0
for i in range(2002):
    for j in range(2002):
        if coor[i][j] == 1:
            tot += 1

print(tot)
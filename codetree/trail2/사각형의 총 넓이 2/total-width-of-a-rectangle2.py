n = int(input())
x1, y1, x2, y2 = [], [], [], [] # 0, 1, 4, 5
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
coor = [[[0] for _ in range(202)] for _ in range(202)]
OFFSET = 100

for i in range(n):
    curr_x1 = y1[i] # 0
    curr_y1 = x1[i] # 1
    curr_x2 = y2[i] # 4
    curr_y2 = x2[i] # 5

    for x in range(curr_x1, curr_x2):
        for y in range(curr_y1, curr_y2):
            coor[OFFSET + x][OFFSET - y] = 1

tot = 0
for i in range(202):
    for j in range(202):
        if coor[i][j] == 1:
            tot += 1

print(tot)

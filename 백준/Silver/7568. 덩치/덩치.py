num = int(input())
value = []

for i in range(num):
    (x, y) = map(int, input().split())
    value.append((x, y))

for i in range(0, num):
    cnt = 1
    for j in range(0, num):
        if(value[i][0] < value[j][0] and value[i][1] < value[j][1]):
            cnt += 1
    print(cnt, end=" ")
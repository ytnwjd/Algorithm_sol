n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
line = [0] * 203
for x1, x2 in segments:
    x1 += 100
    x2 += 100
    for i in range(x1, x2):
        line[i] += 1
    # print(line)

print(max(line))
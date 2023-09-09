import sys
input = sys.stdin.readline

x_li = []
y_li = []
x = 0
y = 0
for _ in range(3):
    a, b = map(int, input().split())
    x_li.append(a)
    y_li.append(b)

for i in range(3):
    if(x_li.count(x_li[i]) == 1):
        x = x_li[i]
    if(y_li.count(y_li[i]) == 1):
        y = y_li[i]
print(x, y)
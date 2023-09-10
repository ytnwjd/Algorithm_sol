import sys
input = sys.stdin.readline

n = int(input())
li_x = []
li_y = []
for i in range(n):
    x, y = map(int, input().split())
    li_x.append(x)
    li_y.append(y)

li_x.sort(); li_y.sort()

if (n == 1):
    print(0)
else:
    x = (li_x[-1]-li_x[0])
    y = (li_y[-1]-li_y[0])
    print(x*y)

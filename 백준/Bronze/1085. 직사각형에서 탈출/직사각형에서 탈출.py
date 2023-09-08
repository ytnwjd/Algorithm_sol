import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())
ans_x = 0
ans_y = 0
if x > (w/2) :
    ans_x = w - x
else :
    ans_x = x
if y > (h/2) :
    ans_y = h - y
else :
    ans_y = y

if (ans_x > ans_y):
    print(ans_y)
else:
    print(ans_x)
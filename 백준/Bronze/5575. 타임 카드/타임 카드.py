import sys
input = sys.stdin.readline

for i in range(3):
    h, m, s, h1, m1, s1 = map(int, input().split())
    a_time = h*60*60 + m*60 + s
    b_time = h1*60*60 + m1*60 + s1
    time = b_time - a_time
    h = time // 60 // 60 % 24
    m = time // 60 % 60
    s = time % 60
    print(h, m, s)
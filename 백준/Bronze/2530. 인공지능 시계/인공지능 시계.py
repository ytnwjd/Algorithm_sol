import sys
input = sys.stdin.readline

h, m, s = map(int, input().split())
time = int(input()) #초 단위임

s += time
if(s >= 60):
    time = s // 60
    s = int(s % 60)
    m += time
    
if (m >= 60):
    time = m // 60
    m = int(m % 60)
    h += time
if (h >= 24):
    h = h % 24
print(h, m, s)

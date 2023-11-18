import sys
input = sys.stdin.readline

time = int(input())

A = time // 300
B = (time % 300) // 60
C = (time % 60) // 10

if (time % 10 != 0):
    print(-1)
else:
    print(A, B, C)
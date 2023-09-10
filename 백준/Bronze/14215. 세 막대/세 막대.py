import sys
input = sys.stdin.readline

num = sorted(map(int, input().split()))
if (num[2] < num[0]+num[1]):    #삼각형 조건 만족
    print(sum(num))
else:
    print((num[0]+num[1])*2 -1)


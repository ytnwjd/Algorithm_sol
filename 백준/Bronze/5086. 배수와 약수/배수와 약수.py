import sys
input = sys.stdin.readline

while True:
    a, b = map(int, input().split())
    res = 0
    ans = ""
    if (a == 0) and (b == 0):
        break

    if (a < b):
        res = (b%a)
        if (res != 0):
            ans = "neither"
        else:
            ans = "factor"
    else:
        res = (a%b)
        if (res != 0):
            ans = "neither"
        else:
            ans = "multiple"
    print(ans)
import sys
input = sys.stdin.readline

for i in range(int(input())):
    q = 0; d = 0; n = 0; p = 0
    money = int(input())

    q = money // 25
    d = (money % 25) // 10
    n = ((money % 25) % 10) // 5
    p = ((money%25) % 10) % 5

    print(q, d, n, p)
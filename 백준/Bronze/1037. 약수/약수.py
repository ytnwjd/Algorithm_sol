import sys
input = sys.stdin.readline

num = int(input())
lcm = list(map(int, input().split()))

print(max(lcm)*min(lcm))
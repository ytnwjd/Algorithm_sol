import sys
input = sys.stdin.readline

num = int(input())
result = 1
for i in range(num):
    result *= (i+1)
print(result)
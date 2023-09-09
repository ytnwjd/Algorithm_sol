import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
cards = list(map(int, input().split()))

dic = {}

for i in cards:
    dic[i] = 0
for j in numbers:
    if j in dic:
        dic[j] = 1
for k in dic:
    print(dic[k], end=" ")
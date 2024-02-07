import sys 
from itertools import combinations
input = sys.stdin.readline

size = int(input())
numbers = list(map(int, input().split()))
tot = set()

for i in range(1, size+1):
    res = combinations(numbers, i)
    
    for j in res:
        tot.add(sum(j))


for i in range(1, 1000001):
    if i not in tot:
        print(i)
        break


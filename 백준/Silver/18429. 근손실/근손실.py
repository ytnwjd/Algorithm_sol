import sys
from itertools import permutations
input = sys.stdin.readline

n, k  = map(int, input().split())   # n일, k만큼 감소
A = list(map(int, input().split()))
for i in range(n):
    A[i] -= k

result = 0

for a in list(permutations(A, n)):
    total = 500
    # print(a)
    for i in a:
        total += i
        if(total < 500):
            break
    if(total >= 500):
        result += 1

print(result)
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
num_list = deque(i for i in range(1, n+1))

print("<", end="")
while True:
    if(len(num_list) < 2 ):
        break

    for _ in range(k-1):
        num_list.append(num_list.popleft()) 
    
    print(num_list.popleft(), end=", ")

print(num_list.popleft(), end=">")
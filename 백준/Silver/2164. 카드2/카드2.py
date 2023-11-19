import sys
from collections import deque
input = sys.stdin.readline

num = int(input())
card = deque([i for i in range(1, num+1)])

while (len(card) != 1):
    card.popleft()
    card.append(card.popleft())

print(card.popleft())
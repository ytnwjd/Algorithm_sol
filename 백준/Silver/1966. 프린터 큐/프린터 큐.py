import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    num, doc = map(int, input().split())
    prior = deque(map(int, input().split()))
    order = deque([i for i in range(num)])

    cnt = 0

    while True:
        if (prior[0] == max(prior)):
            cnt += 1
            if (order[0] == doc):
                print(cnt)
                break
            else:
                del prior[0]
                del order[0]
        else:
            prior.append(prior.popleft())
            order.append(order.popleft())
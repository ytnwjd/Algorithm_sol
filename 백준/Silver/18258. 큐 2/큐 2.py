import sys
input = sys.stdin.readline

n = int(input())
queue = []
rear = 0

for _ in range(n):
    num = list(input().split())

    if num[0] == "push":
        num[1] = int(num[1])
        queue.append(num[1])
    elif num[0] == "pop":
        if (len(queue) > rear):
            print(queue[rear])
            rear += 1
        else:
            print(-1)
    elif num[0] == "size":
        print(len(queue)-rear)
    elif num[0] == "empty":
        if(len(queue) == rear):
            print(1)
            rear = 0
            queue = []
        else:
            print(0)
    elif num[0] == "front":
        if (len(queue) > rear):
            print(queue[rear])
        else:
            print(-1)
    else :      # back
        if (len(queue) > rear):
            print(queue[-1])
        else:
            print(-1)

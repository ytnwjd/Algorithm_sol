import sys
input = sys.stdin.readline

queue = []
rear = -1
for _ in range(int(input())):
    ins = list(map(str, input().split()))
    inst = ins[0]
    
    if (inst == "push"):
        rear += 1
        queue.append(int(ins[1]))
    elif (inst == "pop"):
        if(len(queue) != 0):
            print(queue.pop(0))
        else:
            print(-1)
    elif (inst == "size"):
        print(len(queue))
    elif (inst == "empty"):
        if (len(queue) == 0):
            print(1)
        else:
            print(0)
    elif (inst == "front"):
        if (len(queue) == 0):
            print(-1)
        else:
            print(queue[0])
    elif (inst == "back"):
        if (len(queue) == 0):
            print(-1)
        else:
            print(queue[len(queue)-1])
        

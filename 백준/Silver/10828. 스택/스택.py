import sys
input = sys.stdin.readline

stack = []
for i in range(int(input())):
    ins = list(map(str, input().split()))
    
    if (ins[0] == "push"):
        ins[1] = int(ins[1])
        stack.append(ins[1])
    elif (ins[0] == "pop"):
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack[len(stack)-1])
            stack.pop(len(stack)-1)
    elif (ins[0] == "size"):
        print(len(stack))
    elif (ins[0] == "empty"):
        if(len(stack) == 0):
            print(1)
        else:
            print(0)
    else:   #top
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack[len(stack)-1])

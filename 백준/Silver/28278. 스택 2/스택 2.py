import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    num = list(map(int, input().split()))
    if num[0] == 1:    # push
        stack.append(num[1])
    elif num[0] == 2:  # 맨 위의 정수를 뺴고 출력
        if(len(stack) != 0):
            print(stack[len(stack)-1])
            stack.pop(len(stack)-1)
        else:
            print(-1)
    elif num[0] == 3:  # 정수의 개수 출력
        print(len(stack))
    elif num[0] == 4:  # isempty
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if(len(stack) != 0):
            print(stack[len(stack)-1])
        else:
            print(-1)

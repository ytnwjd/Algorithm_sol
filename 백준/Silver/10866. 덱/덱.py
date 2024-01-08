import sys
input = sys.stdin.readline

li = []

def push_front(number):
    li.insert(0, number) 
    return

def push_back(number):
    li.append(number)
    return

def pop_front():
    if(len(li) == 0):
        print(-1)
    else:
        print(li.pop(0))
    return

def pop_back():
    if(len(li) == 0):
        print(-1)
    else:
        print(li.pop(-1))
    return

def size():
    print(len(li))
    return

def empty():
    if(len(li) == 0):
        print(1)
    else:
        print(0)
    return

def front():
    if(len(li) == 0):
        print(-1)
    else:
        print(li[0])
    return

def back():
    if(len(li) == 0):
        print(-1)
    else:
        print(li[-1])
    return


for _ in range(int(input())):
    inst = list(input().split())

    if (inst[0] == "push_back"):
        push_back(inst[1])
    elif (inst[0] == "push_front"):
        push_front(inst[1])
    elif (inst[0] == "pop_back"):
        pop_back()
    elif (inst[0] == "pop_front"):
        pop_front()
    elif (inst[0] == "size"):
        size()
    elif (inst[0] == "empty"):
        empty()
    elif (inst[0] == "front"):
        front()
    elif (inst[0] == "back"):
        back()
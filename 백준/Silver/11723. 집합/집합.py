import sys 
input = sys.stdin.readline

global S
S = set()

def add(x):
    if x not in S:
        S.add(x)

def remove(x):
    if x in S:
        S.remove(x)

def check(x):
    if x in S:
        print(1)
    else:
        print(0)

def toggle(x):
    if x in S:
        remove(x)
    else:
        add(x)


for _ in range(int(input())):
    inst = list(input().split())
    
    if(inst[0] == "add"):
        add(int(inst[1]))
    elif(inst[0] == "remove"):
        remove(int(inst[1]))
    elif(inst[0] == "check"):
        check(int(inst[1]))
    elif(inst[0] == "toggle"):
        toggle(int(inst[1]))
    elif(inst[0] == "all"):
        S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    elif(inst[0] == "empty"):
        S = set()


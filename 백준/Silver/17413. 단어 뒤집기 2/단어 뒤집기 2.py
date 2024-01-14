import sys
input = sys.stdin.readline

string = input()
stk = []
tag = True

i = 0
while True:
    if(i == len(string)):
        break
    
    if(string[i] == "<"):
        tag = False
        if(len(stk) != 0):
            for w in stk[::-1]:
                print(w, end="")
            print(end="")
            stk = []
        stk.append(string[i])
    elif(string[i] == ">"):
        stk.append(string[i])
        for w in stk:
            print(w, end="")
        stk = []
        tag = True
    elif(string[i] != " "):
        stk.append(string[i])
    elif(tag != False and string[i] == " "):
        for w in stk[::-1]:
            print(w, end="")
        print(end=" ")
        stk = []
    elif(tag == False and string[i] ==" "):
        stk.append(string[i])
    
    i += 1

for w in stk[::-1]:
    if(w != "\n"):
        print(w, end="")

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    string = input()
    chk = 0
    
    for i in string:
        if(i == "("):
            chk += 1
        elif(i == ")"):
            chk -= 1
        
        if(chk < 0):
            break

    if(chk == 0):
        print("YES")
    elif(chk < 0):
        print("NO")
    else:
        print("NO")
import sys
input = sys.stdin.readline

def falin (num):
    num = str(num)
    for i in range(len(num)):
        if (num[i] == num[len(num)-i-1]):
            chk = 1
        else:
            chk = 0
            break
    if(chk == 1):
        print("yes")
    else:
        print("no")


while (True):
    num = int(input())
    if (num == 0):
        break
    falin(num)

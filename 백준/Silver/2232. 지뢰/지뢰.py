import sys
input = sys.stdin.readline

num = int(input())
bomb = [int(input()) for _ in range(num)]

for i in range(num):
    if(num == 1):
        print(1)
    else:
        if(i == 0): #맨 앞의 원소
            if(bomb[i] >= bomb[i+1]):
                print(i+1)
        elif(i == num-1):   #맨 뒤의 원소
            if(bomb[i] >= bomb[i-1]):
                print(i+1)
        elif(bomb[i] >= bomb[i-1] and bomb[i] >= bomb[i+1]):
            print(i+1)


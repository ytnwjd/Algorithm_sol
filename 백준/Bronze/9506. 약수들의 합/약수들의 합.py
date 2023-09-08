import sys
input = sys.stdin.readline

while True:
    li = []
    num = int(input())
    if (num == -1):
        break
    
    for i in range(1, num+1):
        ans = num % i
        if (ans == 0):
            li.append(i)
    
    tot = 0
    li.sort()
    li.pop()
    tot = sum(li)

    if(tot != num): 
        print("%d is NOT perfect." % num)
    else:       # 완전수
        print(num, "=", end=" ")
        print(*li, sep=" + ")
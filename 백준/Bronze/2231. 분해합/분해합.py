num = int(input())

for i in range(1, num+1):   
    ifnum = list(map(int, str(i)))
    if (sum(ifnum) + i) == num:
        print(i)
        break
    if i == num:
        print(0)
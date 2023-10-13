import sys
input = sys.stdin.readline

num, k = map(int, input().split())
num_list = [i for i in range(2, num+1)]
rm_list = []

did = 2
cnt = 1

while (True):
    if(cnt == num):
        break
            
    for i in num_list:
        if(i % did == 0):
            rm_list.append(i)
    
    for j in rm_list:
        if (j in num_list):
            num_list.remove(j)

    cnt += 1
    did += 1
    
print(rm_list[k-1])
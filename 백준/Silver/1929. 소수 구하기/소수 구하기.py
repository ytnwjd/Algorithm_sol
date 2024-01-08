import sys
input = sys.stdin.readline

m, n = map(int, input().split())
num_li = [True] * (n+1)
num_li[0] = False; num_li[1] = False; 

for i in range(2, int(n**0.5)+1):
    if(num_li[i] != False):
        for j in range(i*i, n+1, i):
                num_li[j] = False
            
for num in range(m, n+1):
    if(num_li[num] != False):
        print(num)
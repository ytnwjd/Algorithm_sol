import sys
input = sys.stdin.readline

n = int(input())    #8
amout = list(map(int, input().strip().split()))
k = int(input())    #2

pic = n//k  #4

for i in range(0, n, pic):
    amout[i:i+pic] = sorted(amout[i:i+pic])
 
for num in amout:
    print(num, end=" ")
import sys 
input = sys.stdin.readline

prime = [True] * (1000001)
prime[0] = False
prime[1] = False

for i in range(2, int(1000001*0.5)+1):
    if (prime[i]):
        for j in range(i*i, 1000001, i):
            prime[j] = False


while True:
    num = int(input())
    if (num == 0): break
    
    for i in range(3, (num//2)+1, 2):
        if (prime[i] == True and prime[num-i] == True):
            print("%d = %d + %d" % (num, i, num-i))
            break
    

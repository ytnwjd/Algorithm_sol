import sys
input = sys.stdin.readline

def prime_num(num):
    no = 0
    if num == 1 :
        return False
    
    for i in range(2, num):
        if (num % i == 0):
            no += 1

    if (no == 0):
        return True
    else:
        return False
    
m = int(input())
n = int(input())
numbers = []
cnt = 0; tot = 0

for i in range(m, n+1):
    if (prime_num(i)):
        cnt += 1
        tot += i
        numbers.append(i)

if(cnt == 0):
    print(-1)
else:
    numbers.sort()
    print(tot)
    print(numbers[0])
 
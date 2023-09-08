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


cnt = int(input())
num = list(map(int, input().split()))
ans = 0
for i in num:
    if (prime_num(i)):
        ans += 1
print(ans)
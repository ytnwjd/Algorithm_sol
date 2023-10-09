import sys
input = sys.stdin.readline

def fib(n):
    cnt = 0
    if (n == 1 or n ==2):
        cnt += 1
        return cnt
    else:
        return (fib(n-1) + fib(n-2))

def fibb(n):
    return (n-2)

n = int(input())
print(fib(n), fibb(n))
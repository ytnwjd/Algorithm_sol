import sys
input = sys.stdin.readline

cnt = 1
def fib(n):
    global cnt
    if (n == 1 or n ==2):
        cnt += 1
        return 1
    else:
        cnt += 1
        return (fib(n-1) + fib(n-2))

def fibb(n):
    return (n-2)

n = int(input())
print(fib(n), fibb(n))
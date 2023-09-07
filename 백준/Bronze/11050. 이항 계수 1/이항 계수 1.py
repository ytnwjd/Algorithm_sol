import sys
input = sys.stdin.readline

def factorial(num) :
    if (num > 1):
        return num * factorial(num-1)
    else:
        return 1
    
result = 0
n, k = map(int, input().split())
result = factorial(n) // (factorial(k)*factorial(n-k))
print(result)
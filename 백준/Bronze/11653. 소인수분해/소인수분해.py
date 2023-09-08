import sys
input = sys.stdin.readline

def factorization(num):
    for i in range(2, num+1):
        while (num % i == 0):
            print(i)
            num /= i
 
num = int(input())
factorization(num)
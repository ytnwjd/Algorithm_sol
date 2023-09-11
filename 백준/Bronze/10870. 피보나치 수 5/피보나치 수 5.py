import sys
input = sys.stdin.readline

def fibb (num):
    numbers = [0, 1]
    for i in range(2, num+1):
        numbers.append(numbers[i-2]+numbers[i-1])
    print(numbers[num])

fibb(int(input()))
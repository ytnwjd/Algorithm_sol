import sys
input = sys.stdin.readline

size = int(input())
one = int(input())
numbers = [0, one,]
idx = 1

for floor in range(2, size+1):
    li = list(map(int, input().split()))
    idx += 1
    # print("chk", floor, idx)
    v = li[0] + numbers[idx - (floor-1)]
    numbers.append(v)
    
    for j in range(1, len(li)-1):
        idx += 1
        v = max(li[j] + numbers[idx - (floor)], li[j] + numbers[idx-(floor-1)])
        numbers.append(v)
    
    # print("!", idx)
    idx += 1
    v = li[-1] + numbers[idx - floor]
    numbers.append(v)
    
print(max(numbers))
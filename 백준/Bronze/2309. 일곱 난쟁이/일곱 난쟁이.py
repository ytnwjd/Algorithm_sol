import sys
input = sys.stdin.readline

arr = []
tot = 0
for _ in range(9):
    arr.append(int(input()))

tot = sum(arr)

for i in range(8):
    for j in range(i+1, 9):
        if (tot - arr[i] - arr[j] == 100):
            arr[i] = 0
            arr[j] = 0
            arr.sort()
            
            for num in arr:
                if(num != 0):
                    print(num, end='\n')
            exit()
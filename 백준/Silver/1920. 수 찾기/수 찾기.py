import sys
import math
input = sys.stdin.readline

def binary_search(find_li, val):
    i = 0
    j = len(find_li)    #5

    
    mid = math.ceil((i + j)//2)
    j -= 1
    while True:
    
        # print("mid -", mid, "i -", i, "j -", j)
        if(mid < 0 or mid >= len(find_li)):
            return 0
        if(i == mid or j == mid):
            if(val == find_li[i] or val == find_li[j]):
                return 1
            else:
                return 0

        if (val == find_li[mid]):
            return 1
        elif (val < find_li[mid]):
            j = mid
        else:
            i = mid

        mid = math.ceil((i + j)//2)




n = int(input())
note1 = sorted(list(map(int, input().strip().split())))
m = int(input())
note2 = list(map(int, input().strip().split()))

for j in range(m):
    print(binary_search(note1, note2[j]))
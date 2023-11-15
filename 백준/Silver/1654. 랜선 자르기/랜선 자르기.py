import sys
import math
input = sys.stdin.readline

def binary_search(li, num):
    low = 1
    high = li[-1]

    while (low <= high):
        mid = (low + high) // 2
        maxLen = 0

        for v in li:
            maxLen += (v//mid)

        # print(maxLen)
        if(maxLen >= num):  #조건 만족
            low = mid + 1   # 가장 큰 mid 값 찾기위해 1증가
            # print("low : ", low)
        else:   # 조건 만족 x
            high = mid - 1    # 현재 mid보다 더 작은 값으로 나눠줘야 함
            # print("high : ", high)

    print(high)
   

curr, need = map(int, input().split())
lan = []

for _ in range(curr):
    lan.append(int(input()))
lan.sort()

binary_search(lan, need)
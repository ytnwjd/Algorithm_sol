import sys
input = sys.stdin.readline

def count_zero(num):    # num에 들어있는 2*5의 개수 count
    cnt_5 = 0
    chk = 5

    n = num

    while (chk <= n):     #chk가 더 커지면 끝
        cnt_5 += (num // 5)
        num //= 5
        chk *= 5
    
    return cnt_5


for _ in range(int(input())):
    num = int(input())
    print(count_zero(num))

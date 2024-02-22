import sys 
input = sys.stdin.readline

a, b, c, x, y = map(int, input().split())

# 반반을 사는게 더 이득인 경우 
# a와 b중 적게 사는 종류를 반반으로 채우고, 남은 마리 수를 따로 구매
if(a+b > 2*c): 
    half = min(x, y)

    print(c*half*2 + min(c*2, a)*max(0, x-half) + min(c*2, b)*max(0, y-half))
else:
    print(x*a + y*b)

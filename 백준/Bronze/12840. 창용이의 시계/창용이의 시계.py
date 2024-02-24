import sys 
input = sys.stdin.readline


h,m,s=map(int,input().split())
s=h*3600+m*60+s
q=int(input())
for i in range(q):
    tc=list(map(int,input().split()))
    if tc[0]==1:
        s=s+tc[1]
        if s>=86400:
            s=s%86400
    elif tc[0]==2:
        s=s-tc[1]
        if s<0:
            s %= 86400
    else:#tc[0]==3:
        print(int(s/3600),int((s%3600)/60),int((s%3600)%60))


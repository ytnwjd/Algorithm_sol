A, B, C = map(int, input().split())
if(A==B and A==C and B==C):
    print(10000+A*1000)
elif(A!=B and A!=C and B!=C):
    if(A>=B and A>=C):
        max = A
    elif(B>=A and B>=C):
        max = B
    else:
        max = C
    print(max*100)
else:
    if(A==B):
        print(1000+A*100)
    elif(B==C):
        print(1000+B*100)
    elif(A==C):
        print(1000+C*100)
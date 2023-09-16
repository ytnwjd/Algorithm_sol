import sys
input = sys.stdin.readline


for _ in range(int(input())):
    clos = dict()
    

    for _ in range(int(input())):
        c, type_clo = map(str, input().split())

        if (type_clo not in clos):
            clos[type_clo] = 1
        else:
            clos[type_clo] += 1   
        
    result = 1    
    for i in clos:
        result *= clos[i]+1
    print(result-1)
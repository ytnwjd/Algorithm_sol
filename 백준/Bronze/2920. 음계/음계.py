import sys
input = sys.stdin.readline

dic = {"c":1, "d":2, "e":3, "f":4, "g":5, "a":6, "b":7, "C":8}
asc = [1, 2, 3, 4, 5, 6, 7, 8]
des = [8, 7, 6, 5, 4, 3, 2, 1]

order = list(map(int, input().split()))
if(order == asc):
    print("ascending")
elif(order == des):
    print("descending")
else:
    print("mixed")
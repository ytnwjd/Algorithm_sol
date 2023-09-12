import sys
input = sys.stdin.readline

first = 0
second = 0 
third = 0
four = 0
none = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    if (a>0 and b>0):
        first += 1
    elif(a<0 and b>0):
        second += 1
    elif(a<0 and b<0):
        third += 1
    elif(a>0 and b<0):
        four += 1
    else:
        none += 1
print("Q1: %d" % first)
print("Q2: %d" % second)
print("Q3: %d" % third)
print("Q4: %d" % four)
print("AXIS: %d" % none)

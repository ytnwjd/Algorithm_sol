import sys
input = sys.stdin.readline

def triangle_chk(a, b, c):
    num = [a, b, c]
    num.sort()
    if(num[2] < num[0]+num[1]):
        if(num[0] == num[1] and num[1] == num[2]):
            print("Equilateral")
        elif (num[0] != num[1] and num[1] != num[2] and num[0] != num[2]):
            print("Scalene")
        else:
            print("Isosceles")
    else:
        print("Invalid")


while True:
    a, b, c = map(int, input().split())
    if (a==0 and b==0 and c==0):
        break
    triangle_chk(a, b, c)

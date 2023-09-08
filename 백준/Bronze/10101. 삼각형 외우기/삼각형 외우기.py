import sys
input = sys.stdin.readline

ang1 = int(input())
ang2 = int(input())
ang3 = int(input())

tot = ang1 + ang2 + ang3

if (tot == 180):
    if (ang1 == 60 and ang2 == 60 and ang3 == 60):
        print("Equilateral")
    elif (ang1 != ang2) and (ang2 != ang3) and (ang1 != ang3):
        print("Scalene")
    else:
        print("Isosceles")
else :
    print("Error")
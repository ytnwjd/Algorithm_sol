num = input()
if("A" in num):
    if(num == "A0"):
        print(4.0)
    elif(num == "A-"):
        print(3.7)
    else:
        print(4.3)
elif("B" in num):
    if(num == "B0"):
        print(3.0)
    elif(num == "B-"):
        print(2.7)
    else:
        print(3.3)
elif("C" in num):
    if(num == "C0"):
        print(2.0)
    elif(num == "C-"):
        print(1.7)
    else:
        print(2.3)
elif("D" in num):
    if(num == "D0"):
        print(1.0)
    elif(num == "D-"):
        print(0.7)
    else:
        print(1.3)
else:
    print(0.0)

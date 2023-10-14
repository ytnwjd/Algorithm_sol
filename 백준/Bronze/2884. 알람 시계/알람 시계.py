Hour, Minute = map(int, input().split())
if (Minute < 45):
    if (Hour == 0):
        print("23", Minute+15)
    else:
        print(Hour-1, Minute+15)
else:
    print(Hour, Minute-45)
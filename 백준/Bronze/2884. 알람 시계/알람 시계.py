Hour, Minute = map(int, input().split())
if (Minute < 45):
    Minute_1 = 45-Minute
    if (Hour == 0):
        print("23", 60-Minute_1)
    else:
        print(Hour-1, 60-Minute_1)
else:
    print(Hour, Minute-45)
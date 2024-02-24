while True:
    line = str(input())
    if (line == "END"):
        break
    else:
        print(line[::-1])
a, n = map(int, input().split())
num_list = list(map(int, input().split()))
for x in num_list:
    if(n > x):
        print("{} " .format(x), end="")
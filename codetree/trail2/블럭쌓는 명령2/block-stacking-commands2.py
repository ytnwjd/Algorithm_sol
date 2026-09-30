n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
blank = [0] * n

for kan1, kan2 in commands:
    for i in range(kan1-1, kan2):
        blank[i] += 1

print(max(blank))
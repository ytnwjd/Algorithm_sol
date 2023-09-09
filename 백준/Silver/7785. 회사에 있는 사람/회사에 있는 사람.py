import sys
input = sys.stdin.readline

n = int(input())
people = dict()

for _ in range(n):
    name, chk = map(str, input().split())
    if (chk == "enter"):
        people[name] = chk
    else:
        del people[name]
people = sorted(people.keys(), reverse=True)

for i in people:
    print(i)
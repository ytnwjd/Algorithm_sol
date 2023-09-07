cnt = int(input())
li = []
for i in range(cnt):
    num = int(input())
    li.append(num)
li.sort()
for j in li:
    print(j, end=' ')
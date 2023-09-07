li = [0, 1]
fibb = int(input())

for i in range(2, fibb+1):
    num = li[i-1] + li[i-2]
    li.append(num)
print(li[fibb])
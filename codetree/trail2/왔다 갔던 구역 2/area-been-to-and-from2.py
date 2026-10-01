n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
line = [0] * 2001
curr = 1000


for i in range(n):
    if dir[i] == "R":   # 오른쪽 (+)
        for _ in range(x[i]):
            line[curr] += 1
            curr += 1
    else:   # 왼쪽 (-)
        for _ in range(x[i]):
            curr -= 1
            line[curr] += 1
    
ans = 0
for count in line:
    if count >= 2:
        ans += 1

print(ans)
H, M = map(int, input().split())
Time = int(input())
H += Time//60
M += Time%60
if(M>=60):
    H += 1
    M -= 60
if(H>=24):
    H -= 24
print(H, M)
import sys
input = sys.stdin.readline

n = int(input())
card = [0]
card += list(map(int, input().split()))

cnt = [False] * (n+1)

for i in range(1, n+1):
    cnt[i] = card[i]
    for j in range(1, i+1):
        cnt[i] = min(cnt[i], cnt[i-j] + card[j])

print(cnt[-1])
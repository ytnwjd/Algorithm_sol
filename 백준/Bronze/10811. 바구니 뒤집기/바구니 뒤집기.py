n, m = map(int, input().split())
basket = [ ]
for i in range(n):
    basket.append(i+1)
for _ in range(m):
    i, j = map(int, input().split())
    tmp = basket[i-1:j]
    tmp.reverse()
    basket[i-1:j] = tmp
for id in range(n):
    print(basket[id], end=' ')
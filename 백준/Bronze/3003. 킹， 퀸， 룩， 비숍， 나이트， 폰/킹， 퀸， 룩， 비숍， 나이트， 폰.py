piece = list(map(int, input().split()))
cnt_array = [1, 1, 2, 2, 2, 8]
for i in range(len(piece)):
        piece[i] = (cnt_array[i]- piece[i])
for i in range(len(piece)):
    print(piece[i], end=' ')
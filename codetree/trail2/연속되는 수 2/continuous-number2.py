n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here
max_cnt = 1
temp_cnt = 1

prev = arr[0]
for i in range(1, n):
    if prev == arr[i]:
        temp_cnt += 1
    else:
        prev = arr[i]
        temp_cnt = 1
    
    max_cnt = max(temp_cnt, max_cnt)

print(max_cnt)
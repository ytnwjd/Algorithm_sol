n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
min_dist = float("INF")

for i in range(n):
    temp_dist = 0
    for j in range(n):
        if i != j:
            temp_dist += (A[j]*abs(j-i))
    
    min_dist = min(temp_dist, min_dist)

print(min_dist)
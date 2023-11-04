num_arr = [ ]
div_arr = [ ]
for i in range(10):
    n = int(input())
    if(n in num_arr):
        continue
    else:
        num_arr.append(n)
for j in range(len(num_arr)):
    num = num_arr[j] % 42
    if(num in div_arr):
        continue
    else:
        div_arr.append(num)
print(len(div_arr))
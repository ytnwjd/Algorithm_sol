import sys
input = sys.stdin.readline

def check_num(number):
    num_str = list(str(number))

    if(len(num_str) <= 2):
        return True
    else:
        gap = int(num_str[1]) - int(num_str[0])
        # print(number, gap)
        for i in range(2, len(num_str)):
            temp = int(num_str[i]) - int(num_str[i-1])           
            if(gap != temp):
                return False
        return True
        

n = int(input())
cnt = 0

for i in range(1, n+1):
    # print(i, check_num(i))
    if(check_num(i)):
        cnt += 1

print(cnt)
import sys
input = sys.stdin.readline

string = input()

cnt_0 = string.replace("0", " ")
cnt_0 = cnt_0.split()
cnt_1 = string.replace("1", " ")
cnt_1 = cnt_1.split()

print(min(len(cnt_0), len(cnt_1)))
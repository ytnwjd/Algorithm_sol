import sys
input = sys.stdin.readline

n = int(input())
tot_cnt = 0
for i in range(n):
    word = input()
    rm = []
    for j in range(1, len(word)-1):
        if(word[j] == word[j-1]):
            rm.append(word[j])
            
    for j in rm:
       word = word.replace(j, "", 1)
    word = word.strip()
    
    cnt = 0
    for k in word:
        if (word.count(k) > 1):
           cnt += 1
    
    if (cnt == 0):
        tot_cnt += 1

print(tot_cnt)
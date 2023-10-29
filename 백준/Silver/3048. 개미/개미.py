import sys
input = sys.stdin.readline

n1, n2 = map(int, input().split())
ant1 = list(input().strip("\n"))
ant2 = list(input().strip("\n"))
time = int(input())

ant_dic = dict()
for a in ant1:
    ant_dic[a] = 0
for a in ant2:
    ant_dic[a] = 1

ant1 = ant1[::-1]
ant = ant1 + ant2

tmp = ""
for _ in range(time):
    i = 0
    while (i < len(ant)-1):
        if(ant_dic[ant[i]]==0 and ant_dic[ant[i+1]]==1):
            tmp = ant[i]
            ant[i] = ant[i+1]
            ant[i+1] = tmp
            i += 1
        i += 1

for a in ant:
    print(a, end="")
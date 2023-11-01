n1, n2 = map(int, input().split())
ant1 = list(input().strip())
ant2 = list(input().strip())
t = int(input().strip())

ant1.reverse()
lastIndex = len(ant2)
for i in range(min(t, n1)):
    char = ant1.pop()
    ant2.insert(min(lastIndex, t - i), char)

answer = "".join(ant1 + ant2)
print(answer)
n, m = map(int, input().split())
nameA, nameB = input().split()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
strokes = "32124313113132122212111221"
name = []
remain = []

minLen = min(len(nameA), len(nameB))
if len(nameA) > len(nameB):
    remain = nameA
else:
    remain = nameB

for i in range(minLen):
    name += nameA[i] + nameB[i]

if len(remain) > 0:
    name += remain[minLen:]

for i in range(len(name)):
    name[i] = str(strokes[alphabet.index(name[i])])

while len(name) > 2:
    remain = []
    for i in range(len(name)-1):
        # print("nName", name)
        # print("remain", remain)
        remain.append(str((int(name[i]) + int(name[i+1]))%10))
    
    name = remain

if(str(name[0]) == "0"):
    print(str(name[1])+"%")
else:
    print(str(name[0]) + str(name[1])+"%")
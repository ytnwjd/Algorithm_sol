import sys
input = sys.stdin.readline

num = int(input())
card = [i for i in range(1, num+1)]

while True:
    if (len(card) == 1):
        break

    print(card.pop(0), end=' ')
    card.append(card.pop(0))

print(card[0])
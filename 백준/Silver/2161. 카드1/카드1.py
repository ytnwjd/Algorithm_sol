import sys
input = sys.stdin.readline

num = int(input())
card = [i for i in range(1, num+1)]

while True:
    if (len(card) == 1):
        break

    rm = card.pop(0)
    print(rm, end=' ')
    val = card.pop(0)
    card.append(val)

print(card[0])
vowel = ['a', 'e', 'i', 'o', 'u']
cnt = 0
string = input()
for i in string:
    if (i in vowel):
        cnt += 1
print(cnt)
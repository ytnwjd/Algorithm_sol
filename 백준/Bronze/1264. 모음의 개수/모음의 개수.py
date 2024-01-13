vowel = ['a', 'e', 'i', 'o', 'u']
while(True):
    cnt = 0
    string = input()
    string = string.lower()
    if(string == "#"):
        break
    for i in string:
        if (i in vowel):
            cnt += 1
    print(cnt)
import sys
input = sys.stdin.readline

num, prom = map(int, input().split())
book_s = dict()
book_n = dict()

for i in range(num):
    book_s[input().replace("\n", "")] = str(i+1)

book_n = {v:k for k, v in book_s.items()}   ## k, v 뒤집어서 저장 / v를 이용해 k를 찾는건 전체 순회
# print("s  ",book_s.items())
# print("n  ",book_n.items())

for _ in range(prom):
    ques = input().replace("\n", "")

    if(ques in book_s.keys()):  #문자
        print(book_s[ques])
    else:
        # ques = ques.replace("\n", "")
        print(book_n[ques])

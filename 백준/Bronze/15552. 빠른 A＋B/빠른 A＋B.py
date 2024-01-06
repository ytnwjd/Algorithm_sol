import sys  # 파이썬 인터프린터가 제공하는 변수나 함수를 제어하는 모듈
cnt = int(input())
for c in range(cnt):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)
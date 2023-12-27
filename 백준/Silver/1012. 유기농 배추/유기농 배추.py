import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)    # 재귀 깊이 설정


def search(x, y):   #dfs 사용해 1이면 0로 변경 반환
    if (x < 0 or y < 0 or x >= width or y >= height):
        return False
    
    if (field[x][y] == True):    # 그래프 방문 표시
        field[x][y] = False

        search(x+1, y)  #up
        search(x-1, y)  #down
        search(x, y+1)  #right
        search(x, y-1)  #left

        return True
    


for _ in range(int(input())):
    cnt = 0
    width, height, location = map(int, input().split())
    field = [[False for _ in range(height)] for _ in range(width)]
    
    for _ in range(location):   # 배추 행렬 생성
        x, y = map(int, input().split())
        field[x][y] = True     

    for i in range(width):
        for j in range(height):
            if (search(i, j) == True):
                cnt += 1
    print(cnt)
import sys
from collections import deque
input = sys.stdin.readline

def dfs(start):
    visited[start] = True
    print(start, end=" ")

    for i in range(1, node+1):
        if(graph[start][i] == True and visited[i] == False):    # 아래 노드가 연결되어 있고, 방문하지 않은 경우
            dfs(i)


def bfs(start):
    que = deque([start])
    visited[start] = True

    while que:
        v = que.popleft()
        print(v, end=" ")
        
        for i in range(1, node+1):
            if(graph[v][i] == True and visited[i] == False):    # 다음 노드와 연결되어 있고, 방문하지 않았을 때
                que.append(i)
                visited[i] = True   # 노드 방문



node, edge, num = map(int, input().split())
graph = [[False]*(node+1) for _ in range(node+1)]   # 그래프 행렬 생성

for i in range(edge):
    n1, n2 = map(int, input().split())
    graph[n1][n2] = graph[n2][n1] = True    # 연결되어 있음 
    

visited = [False]*(node+1)  # 방문 확인 list
dfs(num)
print() 

visited = [False]*(node+1) 
bfs(num)

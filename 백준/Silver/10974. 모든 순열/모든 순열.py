import sys
input = sys.stdin.readline

num = int(input())
visited = [False] * (num+1)
result = []

def bt():
    if(len(result) == num):
        print(*result)
        return
    
    for i in range(1, num+1):
        if visited[i] == False:
            result.append(i)
            visited[i] = True
            bt()
            
            result.pop()
            visited[i] = False
            
bt()
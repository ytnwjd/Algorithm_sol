n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
# [흰색 횟수, 검정색 횟수, 현재 색]
line = [[0, 0, "-"] for _ in range(200001)] 
curr = 100000

for i in range(n):
    
    if dir[i] == "L":
        for _ in range(x[i]):
            # 이미 회색인 경우 색상 변경 건너뜀
            if line[curr][2] == "G":
                pass
            elif line[curr][2] == "-":    # 아무색도 안칠해져있으면
                line[curr][2] = "W"       # 흰색
                line[curr][0] += 1
            elif line[curr][2] == "W":    # 이미 흰색이면 (흰색 덧칠)
                line[curr][0] += 1
            elif line[curr][2] == "B":    # 검은색이었으면 흰색으로 변경
                line[curr][2] = "W" 
                line[curr][0] += 1

            # 흰색 2회 이상 AND 검은색 2회 이상이면 회색
            if line[curr][0] >= 2 and line[curr][1] >= 2:
                line[curr][2] = "G"
            
            curr -= 1
        
        # X번 다 이동한 후, 넘어가 버린 1칸을 마지막 도착 위치로 되돌림
        curr += 1
            
    else:   # R
        for _ in range(x[i]):
            # 이미 회색인 경우 색상 변경 건너뜀
            if line[curr][2] == "G":
                pass
            elif line[curr][2] == "-":    # 아무색도 안칠해져있으면
                line[curr][2] = "B"       # 검은색 (수정됨: 0번 -> 1번 카운트)
                line[curr][1] += 1
            elif line[curr][2] == "W":    # 흰색이었으면 검은색으로 변경
                line[curr][2] = "B" 
                line[curr][1] += 1
            elif line[curr][2] == "B":    # 이미 검은색이면 (검은색 덧칠) (수정됨)
                line[curr][1] += 1

            # 흰색 2회 이상 AND 검은색 2회 이상이면 회색
            if line[curr][0] >= 2 and line[curr][1] >= 2:
                line[curr][2] = "G"
            
            curr += 1
            
        # X번 다 이동한 후, 넘어가 버린 1칸을 마지막 도착 위치로 되돌림
        curr -= 1
            
            
white, black, grey = 0, 0, 0

for _, _, color in line:
    if color == "B":
        black += 1
    elif color == "W":
        white += 1
    elif color == "G":
        grey += 1   

print(white, black, grey)
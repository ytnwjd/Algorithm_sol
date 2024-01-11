def solution(array, commands):
    answer = []
    
    for a in commands:
        newArray = []
        for i in range(a[0]-1, a[1]):
            newArray.append(array[i])
            
        newArray.sort()
        answer.append(newArray[a[2]-1])
        
    return answer
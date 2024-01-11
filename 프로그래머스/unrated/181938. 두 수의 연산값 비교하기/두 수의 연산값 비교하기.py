def solution(a, b):
    newCal = int(str(a) + str(b))
    new = 2*a*b
    
    answer = max(newCal, new)
    return answer
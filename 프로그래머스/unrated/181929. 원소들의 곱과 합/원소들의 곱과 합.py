def solution(num_list):
    mul = 1
    for i in num_list:
        mul *= i
        
    tot = sum(num_list)
    tot = tot**2
    
    if(mul < tot):
        answer = 1
    else:
        answer = 0
        
    return answer
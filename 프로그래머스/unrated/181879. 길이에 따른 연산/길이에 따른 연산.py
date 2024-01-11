def solution(num_list):
    mul = 1
    
    if len(num_list) >= 11:
        answer = sum(num_list)
    else:
        for i in num_list:
            mul *= i
        answer = mul
    return answer
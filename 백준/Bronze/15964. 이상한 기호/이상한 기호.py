def cal(num1, num2):
    result = (num1+num2)*(num1-num2)
    return result

a, b = map(int, input().split())
print(cal(a, b))
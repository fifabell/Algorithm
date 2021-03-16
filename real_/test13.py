# 10870_ 피보나치의 수
# input
# 10
# output
# 55

_val = int(input())

def fivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fivo(n-1) + fivo(n-2)
        return result


print(fivo(_val))

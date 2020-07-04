N = int(input())
m = N // 10 # 몫
n = N % 10  # 나머지
f_m = m
f_n = n
count = 0   # 갯수

while 1:
    k = m + n
    m = n
    n = k % 10
    count += 1
    if f_m == m and f_n == n :
        break

print(count)

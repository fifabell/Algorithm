N = int(input())
K = N * 2 - 1
_blank = 0
for i in range(K, 1, -2):
    print(_blank*" "+i*"*")
    _blank += 1

for i in range(1, K+2, 2):
    print(_blank*" "+i*"*")
    _blank -= 1
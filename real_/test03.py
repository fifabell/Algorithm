# 백준 1010번. 다리 놓기
def fact(n):
    a = 1
    for i in range(1, n+1):
        a = a * i
    return a

def solution():
    N, M = map(int, input().split(' '))

    if N == 0 or M == 0 :
        print(0)
        return

    Nfact = fact(N)
    Mfact = fact(M)
    _fact = fact(M - N)

    print(Mfact // Nfact // _fact)

T = int(input())

for i in range(T):
    solution()
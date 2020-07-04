# ing
N, M = map(int,input().split())
P, O = map(int,input().split())

trueKnown = [[] for i in range(O)]
trueKnown[O] = P

print(trueKnown)
# for i in range(M):

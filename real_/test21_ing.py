N,M = map(int,input().split())
arr = [[0 for i in range(N+1)] for j in range(M+1)]
checked = set()
print(arr)

for i in range(M):
    a,b = map(int,input().split())
    arr[b][a] = 1
    checked.add(b)
print(checked)
checked = list(checked)
for i in range(len(checked)):
    print(checked[i])

while checked:
    max = 0
    element = checked.pop(0)
    for i in range(element):
        # arr[]
print(arr)
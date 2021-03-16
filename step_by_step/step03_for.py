N, X = map(int, input().split())
s = []
result = []
s.append(list(input().split()))
for i in range(len(s)):
    t = list(map(int, s[i]))

for i in range(len(t)):
    if t[i] < X:
        result.append(str(t[i]))

print(' '.join(result))

# 1946_신입사원

# input
# 2
# 5
# 3 2
# 1 4
# 4 1
# 2 3
# 5 5
# 7
# 3 6
# 7 3
# 4 2
# 1 4
# 5 7
# 2 5
# 6 1

# output 
# 4
# 3

totalNum = int(input())

for i in range(totalNum):
    case = int(input())
    case1 = [0 for i in range(case)]
    case2 = [0 for i in range(case)]
    case3 = [0 for i in range(case)]
    check = [False for i in range(case)]
    for j in range(case):
        a,b = map(int,input().split())
        case1[j] = a
        case2[j] = b

        print(case1)
        
for i in range(case):
    case3[i] = case2.index(i+1)

print(case3)

totalNum = int(input())
checkList = []
bigCheck = False

for i in range(totalNum):
    st = input().split()
    print(st)
    for j in range(len(st)):
        firstStr = st[j][0]
        if firstStr not in checkList:
            checkList.append(firstStr)
            break
        else:
            for k in range(len(st[j])):
                if st[j][k] in checkList:
                    pass
                else:
                    checkList.append(st[j][k])
                    break

print(checkList)



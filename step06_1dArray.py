for i in range(int(input())):
    li = list(map(int,input().split()))
    avg = int(sum(li[1:])/li[0])
    count = 0
    for j in li[1:]:
        if avg < j:
            count += 1

    print(str('%.3f' % round(count / li[0] * 100, 3)) + "%")

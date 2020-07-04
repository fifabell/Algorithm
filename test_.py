getlist = list(input())
check = [[0] for i in range(4)]
l = []
# result = ''
# for i in getlist:
#     for j in i:
#         if j.istitle():
#             result += j

# # while result:

# # print(getlist.istitle())
# if result == 'UCPC':
#     print("I love UCPC")
# else:
#     print("I hate UCPC")

for i in getlist:
    if i.find('U') != -1 and check[0]==0:
        getlist.remove('U')
        check[0] = 1
        l.append(i)

    elif i.find('C') != -1 and check[1]==0:
        getlist.remove('C')
        check[1] = 1
        l.append(i)

    elif i.find('P') != -1 and check[2]==0:
        getlist.remove('P')
        check[2] = 1
        l.append(i)

    elif i.find('C') != -1 and check[3]==0:
        getlist.remove('C')
        check[3] = 1
        l.append(i)

print(check)


        
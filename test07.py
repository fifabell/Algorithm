N = int(input())

def _1138(N):
    check = [N-i for i in range(N)] # 4 3 2 1    
    result = []

    set_list = list(map(int, input().split())) # 2 1 1 0
    rev_list = list(reversed(set_list))
    for i in range(len(rev_list)):
        result.insert(rev_list[i], check[i])
        # print("input ("+str(rev_list[i])+") = "+str(check[i]))
        # print(result)
    r = ''
    for i in result:
        r += str(i) + " "
    return r

# _1138(N)
print(_1138(N))

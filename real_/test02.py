ip = int(input())

ip_list = list()
for i in range(0, ip):
    ip_list.append(int(input()))
    print(ip_list[i])

def fivo(n):
    if n==1:
        print(1)
        return 1
    elif n==0:
        print(0)
        return 0
    elif n>1 and n<=40:
        return fivo(n-1)+fivo(n-2)
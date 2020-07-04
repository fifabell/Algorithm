totalFriends = int(input())-1
totallists = int(input())
friends = [[] for i in range(totalFriends)]

myFriends = []
for i in range(totallists):
    N,M = map(int,input().split())
    friends[N].append(M)
    if N == 1 :
        myFriends.append(M)
print("friends: "+str(friends))
for i in range(len(myFriends)):
    if friends[myFriends[i]] not in myFriends:
        for val in friends[myFriends[i]]:
            myFriends.append(val)
print("Myfriends: "+str(myFriends))
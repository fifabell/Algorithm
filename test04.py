# 백준 1463. 1로 만들기
X = int(input())
# input값을 받아옵니다.

count = 0
# count를 초기화시켜줍니다. 이 count는 회전수를 나타냅니다.
result = [X]
# input값을 result에 넣어줍니다.

def calculation(x):
    # input값이 x로 들어왔습니다. 
    lst = []
    # for문을 이용해 x에 1을 뺼 경우, x를 3으로 나눌경우, 2로 나눌경우를 각각 배열에 저장합니다.
    for i in x:
        lst.append(i-1)
        if i%3 ==0:
            lst.append(i/3)
        if i%2 ==0:
            lst.append(i/2)
    print(lst)
    lst = set(lst)
    # set()함수는 배열의 중복값을 신경쓰지않고 순서상관없이 배열에 저장합니다.
    lst = list(lst)
    # list()함수는 배열의 중복값을 제거하고 자동 정렬해줍니다.
    return lst
while True:
    # 받아온 input값이 1인지 확인해주고 1일경우 바로 반복문을 빠져나옵니다.
    if X == 1:
        break
    temp = result
    result = []
    # 받아온 input값을 array안에 넣어 calculation()함수에 전달합니다.
    result = calculation(temp)
    count += 1
    # 1회 반복 이후 return받은 lst의 최소값이 1이 아닐경우 이 함수를 반복합니다.
    if min(result) == 1:
        break
print(count)
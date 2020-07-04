N = int(input())
sum = 0
for i in range(0, 5000):
    sum += 1+i
    if N <= sum:
        totalNum = i+2
        startNum = N-(sum-i-1)
        break
if totalNum % 2 == 0:
    result = str(totalNum - startNum) + "/" + str(startNum)
else:
    result = str(startNum) + "/" + str(totalNum - startNum)
    
print(result)
    
    
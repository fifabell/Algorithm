# 13301 _ 타일장식몰 _ 피보나치 응용
# input
# 5
# output
# 26

_val = int(input())
_total = []

for i in range(1,81):
    if i == 1 or i == 2:
        ad = 1
    else :
        ad = _total[i-2] + _total[i-3]
    _total.append(ad)

result = 0
if _val == 1 :
    result = 4
elif _val == 2 :
    result = 6
else :
    result = (_total[_val-1] * 2) + ( _total[_val-1] + _total[_val-2] ) * 2
# result = dulrae(_val)
print(result)

# print(_total)
# ing
inp = int(input())

def _16561(inp):
    cnt = 1
    diff = 1
    result = 1
    if inp == 9:
        print(1)
    if inp % 3 == 0 and inp > 9:
        for i in range(9, inp, 3):
           diff = cnt + diff
           result = result + diff
           if i == inp-3:
               print(result)
    else:
        return False
    
    

_16561(inp)

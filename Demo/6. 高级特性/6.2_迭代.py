def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    
    min = 0
    max = 0
    for x in L:
        if min == 0:
            min = x
        if max == 0:
            max = x

        if min > x:
            min = x
            continue
        if max < x:
            max = x
            continue
    
    return (min, max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
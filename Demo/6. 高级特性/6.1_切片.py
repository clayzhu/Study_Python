def trim(s):
    # if len(s) > 0:
    #     x = 0
    #     while x < len(s):
    #         temp = s[x:x + 1]
    #         if temp != ' ':
    #             s = s[x:]
    #             break
    #         x = x + 1
    #     y = 0
    #     while y < len(s):
    #         temp = ''
    #         if y == 0:
    #             temp = s[-1:]
    #         else:
    #             temp = s[(-y - 1):(-y)]
    #         if temp != ' ':
    #             s = s[:len(s) - y]
    #             break
    #         y = y + 1
    #     if x == len(s) & y == len(s):
    #         s = ''

    if len(s) > 0:
        while s[:1] == ' ':
            s = s[1:]
        while s[-1:] == ' ':
            s = s[:-1]
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

def trim(s):
    if s[:1] is '':
        s1 = s[1:]
        if s1[-2:] is '':
            s2 = s1[:-2]
            return s2
        else:
            return s1
    elif s[-2:] is '':
        s3 = s[:-1]
        return s3
    else:
        return s

if trim('hello   ') != 'hello':
    print('测试失败')
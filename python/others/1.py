# -*- coding: utf-8 -*-
# @Data : 2020-04-03

str01 = 'aabbcdbaaabc'

def remove_ab(s):
    if "ab" in s:
        s = s.replace("ab",'')
        return remove_ab(s)
    return s

s = remove_ab(str01)
print(s)
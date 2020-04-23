# -*- coding: utf-8 -*-
# @Data : 2020-04-23

l = [1,2,3,4,5,6,5,7,8,6,9,5]

d = {}

for i in l:
    try:
        d[i] += 1
    except KeyError:
        d[i] = 1
# print(sorted(d.items(), key=lambda x: x[1])[-1][0])

# d = {True: 'yes', 1: 'no', 1.0: 'maybe'}
# print(d)

# print(True==1==1.0)

xs = dict()
xs[True] = 'yes'
xs[1] = 'no'
xs[1.0] = 'maybe'

# python 字典中键相同的判断逻辑 （只有在 散列值 和 __eq__ 都相同的情况下，才会判断键一致）

# __eq__ 相同， 散列值不同
class AlwaysEqual:

    def __init__(self, other):
        self.other = other

    def __eq__(self, ohter):
        return True

    def __hash__(self):
        return id(self)

# a1 = AlwaysEqual(42)
# a2 = AlwaysEqual("what?")
# print(a1==a2)
# print(hash(a1) == hash(a2))

# print({a1: 'yes', a2: 'no'})

# 散列值相同， __eq__ 不同
class AlwaysHashEqual:

    def __init__(self, other):
        self.other = other

    def __eq__(self, value):
        return False
    
    def __hash__(self):
        return 1

h1 = AlwaysHashEqual(42)
h2 = AlwaysHashEqual('what')
# print(h1==h2)
# print(hash(h1) == hash(h2))

# print({h1: 'yes', h2: 'no'})

# __eq__ 相同，散列值相同
class AlwaysEqHashEqual:

    def __init__(self, other):
        self.other = other
    
    def __eq__(self, value):
        return True
    
    def __hash__(self):
        return 1

e1 = AlwaysEqHashEqual(42)
e2 = AlwaysEqHashEqual('WHAT?')
print(id(e1))
print(id(e2))
print(e1 == e2)
print(hash(e1) == hash(e2))

print({e1: 'yes', e2: 'no'})

        
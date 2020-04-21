# -*- coding: utf-8 -*-
# @Data : 2020-04-21

'''
Python 迭代器实现原理

'''

# 初步实现迭代器
class Repeater:

    def __init__(self, value):
        self.value = value

    # 需要返回带有 __next__ 方法的对象
    def __iter__(self):
        return RepeaterIterator(self)

class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    # 返回每次迭代的值
    def __next__(self):
        return self.source.value

repeater = Repeater("Hello")
itertor = iter(repeater)
print(next(itertor))
print(next(itertor))


# 简化迭代器
class SimpleRepeater:
    def __init__(self, value):
        self.value = value
    
    # 需要返回带有 __next__ 方法的对象，即对象本身
    def __iter__(self):
        return self
    
    def __next__(self):
        return self.value

repeater = SimpleRepeater("World")
itertor = iter(repeater)
print(next(itertor))
print(next(itertor))


# 有限次数的迭代器
class BoundsRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value

repeater = BoundsRepeater("Yes", 3)
# for item in repeater:
#     print(item)
itertor = iter(repeater)
print(next(itertor))
print(next(itertor))
print(next(itertor))
print(next(itertor))

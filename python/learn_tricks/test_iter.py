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
# class BoundsRepeater:
#     def __init__(self, value, max_repeats):
#         self.value = value
#         self.max_repeats = max_repeats
#         self.count = 0

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.count >= self.max_repeats:
#             raise StopIteration
#         self.count += 1
#         return self.value

# repeater = BoundsRepeater("Yes", 3)
# # for item in repeater:
# #     print(item)
# itertor = iter(repeater)
# print(next(itertor))
# print(next(itertor))
# print(next(itertor))
# print(next(itertor))


# 使用生成器改写
def repeater_generator(value):
    while True:
        yield value

# for i in repeater_generator("Hello")
rg = repeater_generator("Hello")
print(rg)
print(next(rg))
print(next(rg))


# 停下来的生成器
def repeater_three_times(value):
    yield value
    yield value
    yield value

# for x in repeater_three_times("World"):
#     print(x)

# rg = repeater_three_times("World")
# print(next(rg))
# print(next(rg))
# print(next(rg))
# print(next(rg))


def bounded_repeater(value, max_repeats):
    # 原始方法
    # count = 0
    # while True:
    #     if count >= max_repeats:
    #         return
    #     count += 1
    #     yield value
    for i in range(max_repeats):
        yield value


# 列表解析式
genexpr = ('Hello' for i in range(3))


# 迭代器链，推荐的设计方法，类似于管道
def integers():
    for i in range(1,9):
        yield i

inter = integers()
print(list(inter))

def squared(seq):
    for i in seq:
        yield i * i

squ = squared(integers())
print(list(squ))

def negated(squ):
    for i in squ:
        yield -i

neg = negated(squared(integers()))
print(list(neg))
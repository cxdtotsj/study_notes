# -*- coding: utf-8 -*-
# @Data : 2020-04-03

import functools
import time

# def get_run_time(*args, **kwargs):
#     def run_time()

def make_adder(n):
    def add_01(x):
        return n+x
    def add_02(x):
        return n-x
    if n > 10:
        return add_01
    else:
        return add_02
    
    real_add = make_adder(9)
    print(real_add(1))


# lamdba
add = lambda x, y: x+y
# print(add(1, 2))


# 装饰器
def null_decorator(func):
    return func

# 多个装饰器修饰
def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def em(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
                f'with {args}, {kwargs}')
        origin_result = func(*args, **kwargs)
        print(f'TRACE: {func.__name__}() '
                f'returned: {origin_result}')
        return origin_result
    return wrapper

# 把字母输出为大写字母
def uppercase(func):
    # 输入闭包内，被装饰函数的名称和注释
    # 所有装饰器上最好都需要添加，便于调试
    @functools.wraps(func)
    def wrapper():
        origin_result = func()
        modified_result = origin_result.upper()
        return modified_result
    return wrapper

import datetime

def run_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        # start_time = datetime.datetime.now()
        print(start_time)
        origin_result = func(*args, **kwargs)
        end_time = time.time()
        # end_time = datetime.datetime.now()
        print(end_time)
        print(f'FUNC: {func.__name__} runed {end_time - start_time}')
        return origin_result
    return wrapper



# @trace
# def say(name, line):
#     """名称"""
#     return f'{name}: {line}'

# say("bear", "chen")


# @null_decorator
# 装饰器从下往上运行
# @strong
# @em
# @uppercase
@run_time
def greet():
    "return a friendly greeting."
    return "Hello"

# print(greet.__name__)
# print(greet.__doc__)
print(greet())
# print(greet())

# print(greet)
# print(null_decorator(greet))
# print(uppercase(greet))


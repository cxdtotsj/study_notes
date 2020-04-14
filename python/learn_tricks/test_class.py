# -*- coding: utf-8 -*-
# @Data : 2020-04-09

'''
第四章 类和面向对象
'''

class Car01:
    def __init__(self, name, mile):
        self.name = name
        self.mile = mile
    
    # 当把对象转换成字符串时调用
    def __str__(self):
        return f'__str__ {self.name}'
    
    # 解释器调用实例对象时会打印
    def __repr__(self):
        return f'__repr__ {self.name}'
# my_car_01 = Car01('bear', 2580)
# print(my_car_01)
# print(repr(my_car_01))


from collections import namedtuple

Car = namedtuple("Car", "color mileage")
# my_car = Car("red", 1234)
# print(my_car)
# print(my_car.color)
# print(my_car.mileage)


class Pizza:
    def __init__(self, ingredints):
        self.ingredints = ingredints
    
    def __repr__(self):
        return f'Pizza({self.ingredints})'
    
    # 适用于构建工厂函数
    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])
    
    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])
    
# print(Pizza.margherita())
# print(Pizza.prosciutto())


class MyClass:

    def __init__(self, init_field):
        self.init_field = init_field
        
    def __repr__(self):
        return f'This is my_class: {self.init_field}'

    def method(self):
        return 'instance method called', self
    
    @classmethod
    def class_method(cls):
        return 'class method  called', cls('green')
    
    @staticmethod
    def static_method():
        return 'static method called'

my_class = MyClass('red')
print(my_class.method())
print(my_class.class_method())
print(my_class.__class__.class_method())
print(my_class.static_method())
print(MyClass.class_method())
print(MyClass.static_method())
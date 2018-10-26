'''
5.5、 __call__ 用法
'''

import random

class BingoCage:

    def __init__(self,items):
        self._items = list(items)
        random.shuffle(self._items) # 随机打乱序列
    
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


if __name__ == "__main__":
    bingo = BingoCage(range(10))
    print(bingo())
    print(bingo())
    print(bingo())
    print(bingo())
    print(callable(bingo)) # 判断是否是可调用对象
    
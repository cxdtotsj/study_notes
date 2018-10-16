import json
import functools


class Drcorator:
    '''装饰器的引用'''

    @classmethod
    def json_out(self,indent=None,sort_keys=False):
        def actual_decorator(decorated):
            def inner(*arg,**kw):
                result = decorated(*arg,**kw)
                return json.dumps(result,indent=indent,sort_keys=sort_keys)
            return inner
        return actual_decorator



def log(func):
    @functools.wraps(func)  # 保证被装饰函数func的__name__属性不变
    def wapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wapper

@log
def now():
    print('2018-03-02')

now()


# 自定义文本
def log_text(text):
    def decorator(func):
        @functools.wraps(func)  # 保证被装饰函数func的__name__属性不变
        def wapper(*args,**kw):
            print('%s %s():' %(text,func.__name__))
            return func(*args, **kw)
        return wapper
    return decorator

@log_text("execute")
def now_text():
    print('2018-9-26')

now_text()

print(now_text.__name__)


'''请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：'''
import time,functools

def metric(func):
    def get_time(*args, **kw):
        start_time = time.time()
        name = func(*args, **kw)
        end_time = time.time()
        print('time is: %s' %(end_time-start_time))
        return name
    return get_time


@metric
def fast(a,b):
    time.sleep(2)
    return a

x = fast(2,1)
print(x)
import logging
'''
def use_logging(func):
    logging.warn("%s is running" % func.__name__)
    func()

def foo():
    print('i am foo')

use_logging(foo)
'''


def use_logging(func):
    def wrapper():
        logging.warn("%s is running" % func.__name__)
        func() #  把 foo 当做参数传递进来时，执行func()就相当于执行foo()
    return wrapper

def foo():
    print('i am foo')

foo = use_logging(foo)  # 因为装饰器 use_logging(foo) 返回的时函数对象 wrapper，这条语句相当于  foo = wrapper
foo() #  这里在调用foo()的时候只执行了wrapper()


'''
def use_logging(func):
    def wrapper():
        logging.warn("%s is running" % func.__name__)
        func() #  把 foo 当做参数传递进来时，执行func()就相当于执行foo()
    return wrapper

@use_logging #  语法糖，相当于外裤
def foo(): #  相当于内裤
    print('i am foo')

foo() #  这里在调用foo()的时候也执行了wrapper()
'''

'''
lst = [1,2,3,4,5]
lst1 = [i**2 for i in range(0,len(lst))]
print(lst1)
'''
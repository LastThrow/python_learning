"""
def fun():
    f = open("1.txt",'w')
    try:
        f.write("python is the best advanced language")
    except IOError:
        print("oop error")
    except Exception:
        print('....')
    finally:
        f.close()


def fun():
    # 将open函数的返回值交给f
    with open('1.txt', 'w') as f:
        f.write("python is the best advanced language")

"""


class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print('__enter__')
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, *args):
        print('__exit__')
        self.f.close()


def main():
    file = File('1.txt', 'w')
    # 以下用到上下文管理器
    # with首先查看file是一个具有__enter__和__exit__方法的实例对象，然后调用__enter__方法，将此方法的返回值给f
    # 不管with语句内是否产生异常，都会调用file对象中的__exit__方法
    # 用with时要保证文件能打开，比如以写方式打开
    with file as f:
        print('writing...')
        f.write('python is the best advanced language')


if __name__ == '__main__':
    main()

"""
from contextlib import contextmanager

@contextmanager
def my_open(path, mode): 
    f = open(path, mode)  # 当my_open()函数被调用时仅仅执行到yield之前的语句
    yield f  # 此时yield返回f
    f.close()
    
调用
with my_open('out.txt', 'w') as f:  # with将yield的返回值给f
    f.write("hello Mr.shen")  # 在执行过程中异常或执行完成，则再去执行yield后面的语句
"""
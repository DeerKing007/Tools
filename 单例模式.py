import threading

# 用元类实现单例模式
class SingletonMeta(type):
    """自定义元类"""
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        cls.__lock = threading.Lock()
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance

class President(metaclass=SingletonMeta):
    """总统(单例类)"""
    pass


# 利用装饰器来实现一个单例模式

def A(cls):
    ab = {}

    def a(*args, **kargs):
        if cls not in ab:
            ab[cls] = cls(*args, **kargs)
        return ab[cls]

    return a


@A
class B(object):
    pass

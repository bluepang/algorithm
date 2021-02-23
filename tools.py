import functools


# 装饰器，用来计算函数运行时间
def print_exce_time(func):
    from time import time, sleep
    @functools.wraps(func)
    def innner(*args, **kwargs):
        start = time()
        ret = func(*args, **kwargs)
        # sleep(1)
        end = time()
        print('{0}() execute time: {1:.2}ms'.format(func.__name__, (end-start) * 1000))
        return ret

    return innner
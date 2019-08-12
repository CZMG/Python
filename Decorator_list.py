import time
from functools import wraps


def running_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print("running time is: %s" % (end - start))
        return res
    return wrapper

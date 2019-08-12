import time
from functools import wraps

#
# def tt(func):
#     @wraps(func)
#     def t(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         end = time.time()
#         print("running time is: %s" % (end - start))
#         return res
#     return t


# @tt
# def p():
#     print("Start:")
#     time.sleep(2)
#     return print('Hello, world!')
#
#
# # print(p())
# # help(p)
# p()
rz = [
    {'username': 'suguang', 'password': '123'},
    {'username': 'wangshuai', 'password': 'wasd'},
    {'username': 'zhangfan', 'password': '1q2w'}
]
status = {'username': None, 'login': False}
login_name = status['username']


def detected(func):
    @wraps(func)
    def f(*args, **kwargs):
        global status
        if status['login'] is False:
            name = input("name: ")
            password = input("password: ")
        for i in rz:
            # nonlocal name, password
            if name == i['username'] and password == i['password']:
                status['username'] = name
                status['login'] = True
                break
        else:
            print("Username or password is wrong.")

        res = func(*args, **kwargs)
        return res

    return f


@detected
def index():
    print("Welcome to TB, %s" % login_name)


@detected
def home():
    print("Welcome to %s's home." % login_name)


@detected
def gwc():
    print("Welcome to %s's shopping car." % login_name)


index()
# home()
# gwc()

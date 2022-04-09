# https://qiita.com/_rdtr/items/d3bc1a8d4b7eb375c368

class method:
    def __init__(self) -> None:
        self.arg = "arg"
        self.keys = "keys"
        pass

    def __class__(self) -> None:
        pass

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def apply(self, func, x, y):
        return func(x, y)


def wrapper(func):
    def checker(a, b):
        _add = func(a, b)
        _add += 3
        return _add
    return checker


@wrapper
def add(x, y):
    return x + y


print("decorate: ", add(3, 4))

# 上と同義
# add = wrapper(method.add)
# print("not decorate: ", add(3, 4))


def deco(func):
    def wrapper(*args, **kwargs):
        print('--start--')
        func(*args, **kwargs)
        print('--end--')
    return wrapper


@deco
def test():
    print("Hello Decorator")

def logger(func):
    def inner(*args, **keyargs):
        print("Arguments were: %s, %s" % (args, keyargs))
        return func(*args, **keyargs)
    return inner


@logger
def foo1(x, y=2):
    return x * y


@logger
def foo2():
    return 2


def test():
    return foo1(2, 3)

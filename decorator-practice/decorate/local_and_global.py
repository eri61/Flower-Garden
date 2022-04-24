# https://qiita.com/_rdtr/items/d3bc1a8d4b7eb375c368
text = "I am global!"


def foo(arg, b="2", c=True):
    # local変数がglobalより優先される
    # text = 'I am local!'
    print(locals())
    print(text)


def outer(x):
    # 関数のネスト

    def inner():
        # globalから変数xを探す
        print(x)
    inner()
    return 3


def outer_func(some_func):
    # functionも変数の様に扱える
    def inner():
        print("before some_func")
        ret = some_func()
        return ret + 1
    # return definition
    return inner


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Coord: " + str(self.__dict__)

    def test(self):
        return repr(self)


def test():
    # Coordinate(3, 4).test()に同じ
    s = Coordinate(3, 4)
    return repr(s)

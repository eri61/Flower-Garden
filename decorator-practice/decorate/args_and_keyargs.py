# https://qiita.com/_rdtr/items/d3bc1a8d4b7eb375c368

def add(x, y):
    return x + y


def one(*args):
    print(args)


def test():
    # 引数に*lstを渡すことでリストをアンパックしてくれる
    lst = [3, 4]
    _add = add(*lst)
    return _add


def test():
    # dic型もアンパックに対応
    dct = {'x': 1, 'y': 2}
    return add(**dct)

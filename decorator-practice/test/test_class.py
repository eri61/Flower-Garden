import sys

# コメントの後に# noqa（または# nopepだが、環境による）をつけると自動成型を無視する
sys.path.append('..')
from decorate.def_class import testClass  # noqa
from decorate.practice_property import PropertyClass  # noqa


def test_add_func():
    one = testClass(20)
    other = testClass(10)
    return one + other


def test_repr() -> None:
    a = testClass('a')
    twelve = testClass(12)
    print(a, twelve)


def test_call() -> None:
    val = testClass(10)
    return val()


def test_getitem() -> None:
    x = testClass(item={'year': 2022, 'my_name': 'eri68', 'location': 'Flower_Garden'})
    y = testClass(item={'year': 2022, 'location': 'Flower_Garden'})
    print(x['location'])
    print(y['location'])


def test_setitem():
    x = testClass().items
    x['おにぎり'] = 'お米'
    x['オレンジジュース'] = '水'
    return x


def test_iter():
    x = testClass(max=2)
    i = list(x)
    return i


def test_property():
    prop = PropertyClass("it is instance")
    print(prop.message)
    print("change property->")
    prop.message = "make a new instance"
    print(prop.message)


test_property()

from functools import cache, cached_property

"""
@property: 値の参照時に呼び出されるメソッド
@<func>.setter: 値の代入時に呼び出されるメソッド
@cached_property: 中で呼び出されているself.<func>に代入を行わない
"""


@cache
def factorial(n):
    # @cache：入れ子型のモジュール
    # 階乗の関数
    return n * factorial(n-1) if n else 1


# Using @property

# A sample class
class Sample_property():

    def __init__(self):
        self.result = 50

    @property
    # a method to increase the value of
    # result by 50
    def increase(self):
        self.result = self.result + 50
        return self.result


# Using @cached_property


# A sample class
class Sample_caches_property:

    def __init__(self):
        self.result = 50

    @cached_property
    # a method to increase the value of
    # result by 50
    def increase(self):
        self.result = self.result + 50
        return self.result


def test():
    # obj is an instance of the class sample
    print("Using property")
    obj = Sample_property()
    print(obj.increase)
    print(obj.increase)
    print(obj.increase)

    # obj is an instance of the class sample
    print("Using cache_property")
    obj = Sample_caches_property()
    print(obj.increase)
    print(obj.increase)
    print(obj.increase)

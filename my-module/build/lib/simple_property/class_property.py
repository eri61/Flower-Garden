def define_property(self, name, value=None):
    # "_User__name" のような name mangling 後の名前.
    field_name = "_{}__{}".format(self.__class__.__name__, name)

    # 初期値を設定する.
    setattr(self, field_name, value)

    # getter/setter を生成し, プロパティを定義する.
    def getter(_): return getattr(self, field_name)
    def setter(_, value): return setattr(self, field_name, value)
    setattr(self.__class__, name, property(getter, setter))


def define_property(*names):
    def decorator(constructor):
        def wrapper(self, **kwargs):
            for name in names:
                define_property(self, name, kwargs.get(name))
            constructor(self, **kwargs)
        return wrapper
    return decorator

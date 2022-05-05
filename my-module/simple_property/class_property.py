class self_variable:
    def __init__(self, *names) -> None:
        self.names = names

    def def_property(self, name, value=None):
        # "_User__name" のような name mangling 後の名前.
        self.field_name = "_{}__{}".format(self.__class__.__name__, name)

        # 初期値を設定する.
        setattr(self, self.field_name, value)

        # getter/setter を生成し, プロパティを定義する.
        def getter(_): return getattr(self, self.field_name)
        def setter(_, value): return setattr(self, self.field_name, value)
        setattr(self.__class__, name, property(getter, setter))

    def simple_prop(self, constructor):
        names = self.names
        def_property = self.def_property

        def wrapper(self, **kwargs):
            for name in names:
                def_property(name, kwargs.get(name))
            constructor(self, **kwargs)
        return wrapper

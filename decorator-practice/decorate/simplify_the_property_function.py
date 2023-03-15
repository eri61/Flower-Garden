
"""
propertyを簡単に表記する方法
"""
# method 1


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


class User():
    @self_variable("name", "email").simple_prop
    def __init__(
        self, name: str = None, email: str = None
    ) -> None:
        self.name = name
        self.email = email


class User2:
    def __init__(self, *, name=None, email=None):
        self.name = self_variable().def_property("name", name)
        self.email = self_variable().def_property("email", email)


user = User()
user.name = 'eri'
print(f"name: {user.name}   email: {user.email}")

user2 = User2()
user2.name = 'eri'
print(f"name: {user2.name}   email: {user2.email}")

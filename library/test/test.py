from simple_property import define_property


class MyClass:
    @define_property("x", "y")
    def __init__(self) -> None:
        self.x = None
        self.y = None
        pass


myclass = MyClass()
myclass.x = 3
myclass.y = 4
print(f"x: {myclass.x}, y: {myclass.y}")

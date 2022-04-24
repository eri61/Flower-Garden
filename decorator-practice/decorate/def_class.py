class testClass:
    def __init__(self, value=int, item={}, max=0) -> None:
        self.value = value
        self.items = item
        self.max = max
        pass

    def __del__(self):
        # super().__del__()  # 基底クラスに__del__メソッドがあれば必ず呼び出す
        print('__del__')  # インスタンスが破壊されるときに行う処理

    def __call__(self):
        print(f"value is {self.value}")  # 自分の名前を出力する

    def __repr__(self):
        # オブジェクト名のみを入力するとobject.__repr__()が呼ばれる
        return f"value is {str(self.value)} (via __repr__)"

    def __str__(self) -> str:
        #  print() を経由すると__str__()が呼ばれる
        return f"value is {str(self.value)} (via __str__)"

    def __add__(self, other) -> float:
        print("add関数を使用しました")
        return self.value + other.value

    def __getitem__(self, key):
        # t = testClass(<>)
        # t['...']の様に扱うときに呼び出されるメソッド
        if not (key in self.items.keys()):
            raise Exception("key error")
        elif not ('my_name' in self.items.keys()):
            print('お前は誰だ')
        return self.items.get(key)

    def __setitem__(self, key, val):
        self.item[key] = val

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

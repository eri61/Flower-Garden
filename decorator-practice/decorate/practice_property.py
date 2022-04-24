"""
    @property: 
    self.<>で定義したインスタンスを外部処理で変更できるようにするdecorater


    def プロパティ名(self):
    処理

    'プロパティの値を取り出すメソッドを定義する'
    @property
    def プロパティ名(self):
    return 値
 
    'プロパティの値を設定'
    @プロパティ名.setter
    def プロパティ名(self, 値)
    値を設定する処理
 
"""


class PropertyClass:
    def __init__(self, msg) -> None:
        self.message = msg

    def __str__(self) -> str:
        print("call __str__ module")
        return self.message


@property
def message(self):
    return self.__message


@message.setter
def message(self, value):
    if value != "":
        self.__message = value

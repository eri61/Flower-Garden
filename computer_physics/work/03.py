"""
補足
変数指定の際に":"を用いることで変数を宣言することが出来る(推奨)。
※ただし、宣言したからと言って数値の型が変更出来る訳ではない

a:int = 3
a:float = 3.    # or a:float = 3.0
a:str = "3"
a:complex = 1.0 + 2.0J
# etc
"""


def perimeter(height: float, width: float,
              digit: int = 2) -> float:
    prm = 2 * (height + width)
    return round(prm, digit)


def area(height: int, width: int,
         digit: int = 2) -> float:
    ar = height * width
    return round(ar, digit)


_perimeter = perimeter(3.25, 5.27)
_area = area(3.25, 5.72)

print(
    f"The perimeter of a rectangle (height: 3.25, width: 5.72) is {_perimeter}"
)
print(
    f"The area of a rectangle (height: 3.25, width: 5.72) is {_area}"
)

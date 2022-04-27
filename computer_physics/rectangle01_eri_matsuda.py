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

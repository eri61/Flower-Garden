"""
10の位の値を取得して場合分けを行う
60以下 -> 5 : F
61~70 -> 6 : D
...
91~100 -> 9 : A
"""
# answer 1
score = int(input("Enter your score:"))
if score <= 60:
    grade = 'F'
elif score > 60 & score <= 70:
    grade = 'D'
elif score > 70 & score <= 80:
    grade = 'C'
elif score > 80 & score <= 90:
    grade = 'B'
else:
    grade = "A"

print(f"Your grade is {grade}")


# answer 2  ※strを使って条件分岐
grade = {"5": "F", "6": "D", "7": "C", "8": "B", "9": "A"}
score = int(input("Enter your score:"))
ajustement_score = str(score - 1)

if int(ajustement_score) <= 59:
    ajustement_score = "50"

# 先頭の数字でグレード分け
your_grade = grade[ajustement_score[0]]
print(f"Your grade is {your_grade}")

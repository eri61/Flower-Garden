"""
10の位の値を取得して場合分けを行う
60以下 -> 5 : F
61~70 -> 6 : D
...
91~100 -> 9 : A
"""

grade = {"5": "F", "6": "D", "7": "C", "8": "B", "9": "A"}
score = int(input("Enter your score:"))
ajustmented_score = str(score - 1)

if int(ajustmented_score) <= 59:
    ajustmented_score = "50"

your_grade = grade[ajustmented_score[0]]
print(f"Your grade is {your_grade}")

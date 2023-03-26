from statistics import mean

fin = open("input01.dat", "rt")
numbers = list(map(int, fin))
_sum = sum(numbers)
_ave = mean(list(numbers))

print(f"sum = {_sum:.2f} \naverage = {_ave:.2f}")

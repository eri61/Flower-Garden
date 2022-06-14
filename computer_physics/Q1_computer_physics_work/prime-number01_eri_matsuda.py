def prime(num):
    cnt = 0
    for i in range(2, num):
        cnt += (num % i) == 0
    return cnt == 0


def get_prime_list(min: int, max: int) -> list:
    judge = []
    for val in range(min, max):
        if prime(val):
            judge.append(val)
    return judge


get_prime_list(50, 150)

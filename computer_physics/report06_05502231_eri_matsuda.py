import sys
from functools import cache

sys.setrecursionlimit(15000)
# 計算に時間がかかるので、没


def get_prime_list(min: int, max: int) -> list:
    judge = []
    for val in range(min, max):
        if prime(val).discriminator():
            judge.append(val)
    return judge


class prime:
    def __init__(self, num) -> None:
        self.den, self.mol, self.judge = num, num-1, 0

    def discriminator(self):
        '''
        素数判定器
        '''
        return self.prime_or(self.mol)

    @cache
    def prime_or(self, molecule: int) -> bool:
        '''
        self.den: 分母
        molecule: 分子。denominator以下の整数。

        return: bool
            self.denがmolecule以下の全ての自然数(1以外)で割り切れないか
        '''
        if molecule > 1:
            # 割り切れる → +=1：割り切れない→ +=0
            self.judge += (self.den % molecule) == 0
        else:
            return self.judge == 0

        return self.prime_or(molecule=molecule - 1)


get_prime_list(50, 150)

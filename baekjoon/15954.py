import math
from decimal import Decimal


def _f_mean(values):
    return Decimal(sum(values)) / Decimal(len(values))


def _f_std(values):
    _sum = Decimal(0.0)
    _mean = _f_mean(values)

    for p in range(0, len(values)):
        diff = values[p] - _mean
        _sum += diff * diff

    sd = math.sqrt(_sum / (len(values)))
    return sd


if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    result = Decimal(1000.0)
    for i in range(0, n - k + 1):
        tmp = []
        for j in range(0, k):
            tmp.append(Decimal(arr[j + i]))

        std = Decimal(_f_std(tmp))
        if result > std:
            result = std

    print(result)

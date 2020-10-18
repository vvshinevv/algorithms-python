from decimal import Decimal

if __name__ == '__main__':
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    sums = [0 for i in range(N + 1)]
    exps = [0 for i in range(N + 1)]

    for i in range(1, len(arr) + 1):
        sums[i] = sums[i - 1] + arr[i - 1]
        exps[i] = exps[i - 1] + arr[i - 1] ** 2

    re = Decimal('INF')

    for i in range(K, N + 1):
        for j in range(N - i + 1):
            mean = Decimal(sums[i + j] - sums[j]) / i
            var = Decimal(exps[i + j] - exps[j]) / i - mean * mean
            re = min(re, var)

    print(re.sqrt())

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    big1 = arr[n - 1]
    big2 = arr[n - 2]

    chunk = int(m / (k + 1))
    left = int(m % (k + 1))

    result = chunk * big1 * k + chunk * big2 + left * big2
    print(result)
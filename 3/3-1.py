if __name__ == '__main__':
    n = 1260
    count = 0
    change = [500, 100, 50, 10]
    for coin in change:
        count += int(n / coin)
        n %= coin

    print(count)

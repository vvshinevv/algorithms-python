if __name__ == '__main__':
    n = input()
    x = int(ord(n[0]) - ord('a')) + 1
    y = int(n[1])

    steps = [(-2, -1), (-2, 1), (-1, 2), (-1, -2), (1, 2), (1, -2), (2, 1), (2, -1)]

    result = 0
    for step in steps:
        if (0 < x + step[0] <= 8) and (0 < y + step[1] <= 8):
            result += 1

    print(result)

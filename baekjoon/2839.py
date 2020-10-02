if __name__ == '__main__':
    n = int(input())

    result = 0
    flag = n // 5
    for i in range(0, flag + 1):
        tmp = 0
        do = n - i * 5
        if do % 3 == 0:
            tmp += i + do // 3
            if result == 0:
                result = tmp
            else:
                if result > tmp:
                    result = tmp

    if result == 0:
        print(-1)
    else:
        print(result)

if __name__ == '__main__':

    _2017 = [0, 1, 3, 6, 10, 15, 21]
    _2018 = [0, 1, 3, 7, 15, 31]
    p_2017 = [0, 5_000_000, 3_000_000, 2_000_000, 500_000, 300_000, 100_000]
    p_2018 = [0, 5_120_000, 2_560_000, 1_280_000, 640_000, 320_000]

    T = int(input())
    arr = []
    for i in range(T):
        arr.append(list(map(int, input().split())))

    for i in range(len(arr)):
        r_2017 = 0
        r_2018 = 0
        for j in range(1, len(_2017)):
            th = arr[i][0]
            if th == 0:
                break

            if th > 21:
                break
            if _2017[j] >= th:
                r_2017 = p_2017[j]
                break

        for j in range(1, len(_2018)):
            th = arr[i][1]
            if th == 0:
                break

            if th > 31:
                break
            if _2018[j] >= th:
                r_2018 = p_2018[j]
                break

        print(r_2017 + r_2018)

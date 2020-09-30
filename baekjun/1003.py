def add(fir, sec):
    var1 = fir[0] + sec[0]
    var2 = fir[1] + sec[1]
    return [var1, var2]


if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))

    result_dic = {}
    for i in range(max(arr) + 1):
        if i == 0:
            result_dic[i] = [1, 0]
        elif i == 1:
            result_dic[i] = [0, 1]
        else:
            result_dic[i] = add(result_dic[i - 1], result_dic[i - 2])

    for i in arr:
        print(result_dic[i][0], result_dic[i][1])

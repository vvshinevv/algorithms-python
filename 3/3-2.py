if __name__ == '__main__':
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    big1 = arr[n - 1]
    big2 = arr[n - 2]
    result = 0
    flag = k
    for i in range(m):
        if flag == 0:
            result += big2
            flag = k
        else:
            result += big1
            flag -= 1
    print(result)

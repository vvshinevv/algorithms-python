if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        d = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(0, m + 1):
            d[1][i] = i
        for i in range(2, n + 1, 1):
            for j in range(i, m + 1, 1):
                for k in range(j, i + 1, -1):
                    d[i][j] += d[i - 1][k - 1]
        print(d[n - 1][m - 1])

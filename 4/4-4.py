"""
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

5 5
1 1 0
1 1 1 1 1
1 0 1 0 1
1 0 1 0 1
1 0 0 0 1
1 1 1 1 1
"""


def turn_left(di):
    di -= 1
    if di == -1:
        di = 3
    return di


if __name__ == '__main__':
    n, m = map(int, input().split())
    x, y, eye = map(int, input().split())
    result = 0
    g_map = []
    for i in range(n):
        g_map.append(list(map(int, input().split())))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    result = 1
    move_limit = 0
    while move_limit != 4:
        direction = turn_left(eye)
        temp_x = x + dx[direction]
        temp_y = y + dy[direction]

        if g_map[temp_x][temp_y] == 1:
            move_limit += 1
            eye = direction
            continue
        else:
            g_map[x][y] = 1
            x = temp_x
            y = temp_y
            move_limit = 0
            result += 1

    print(result)

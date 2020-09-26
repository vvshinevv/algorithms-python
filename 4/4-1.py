if __name__ == '__main__':
    n = int(input())
    move_list = input().split()
    x, y = 1, 1
    for i in range(len(move_list)):
        if move_list[i] == 'R':
            if y == n:
                continue
            else:
                y += 1
        elif move_list[i] == 'L':
            if y == 1:
                continue
            else:
                y -= 1
        elif move_list[i] == 'U':
            if x == 1:
                continue
            else:
                x -= 1
        else:
            if x == n:
                continue
            else:
                x += 1

    print(x, y)

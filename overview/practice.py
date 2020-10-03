def print_param(name):
    print(f'Hi, {name}')


def dictionary():
    data = dict()
    data['사과'] = 'Apple'
    data['바나나'] = 'Banana'
    data['코코넛'] = 'Coconut'
    if '사과' in data:
        print('데이터 존재')

    print(list(data.keys()))
    print(data.values())


def input_test():
    a, b, c, d, e = map(int, input().split())
    print(a, b, c, d, e)


def input_2_test():
    n = int(input())
    m = int(input())

    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))


if __name__ == '__main__':
    arr = [[0] * 4 for _ in range(3)]
    print(arr)
    # print_param('PyCharm')

    # dictionary()
    # input_test()
    # input_2_test()

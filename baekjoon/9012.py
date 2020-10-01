if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(input()))

    stack = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if '(' == arr[i][j]:
                stack.append(arr[i][j])
            else:
                if len(stack) == 0:
                    stack.append(arr[i][j])
                    break
                else:
                    stack.pop()

        if len(stack) == 0:
            print("YES")
        else:
            print("NO")
            stack.clear()

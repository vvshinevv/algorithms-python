def dfs_1(graph, v):
    stack = [v]
    visited[v] = True
    print(v, end=' ')
    while stack:
        for i in range(len(graph[v])):
            nxt = graph[v][i]
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)
                v = nxt
                print(v, end=' ')
                break
            if i == len(graph[v]) - 1:
                stack.pop()
                if stack:
                    v = stack[-1]


def dfs_2(graph, v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs_2(graph, i)


if __name__ == '__main__':
    d_map = [
        [],
        [2, 3, 8],
        [1, 7],
        [4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
    ]
    visited = [False] * 9
    dfs_2(d_map, 1)

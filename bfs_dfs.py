import sys
from collections import deque
input = sys.stdin.readline


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)
    return order


def dfs(graph, start, visited, order=None):
    if order is None:
        order = []
    visited[start] = True
    order.append(start)
    for nxt in graph[start]:
        if not visited[nxt]:
            dfs(graph, nxt, visited, order)
    return order


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)
    print(*bfs(graph, 1, visited))

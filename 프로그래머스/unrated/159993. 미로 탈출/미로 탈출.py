from collections import deque


def solution(maps):
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    h, w = len(maps), len(maps[0])

    def in_boundary(y, x):
        return 0 <= y < h and 0 <= x < w

    def bfs(start, end):
        memo = [[False for _ in range(w)] for _ in range(h)]
        q = deque([])

        for y in range(h):
            for x in range(w):
                if maps[y][x] == start:
                    q.append((y, x, 0))

        while q:
            y, x, cost = q.popleft()

            if maps[y][x] == end:
                return cost

            for dy, dx in direction:
                ny, nx = y + dy, x + dx

                if in_boundary(ny, nx) and maps[ny][nx] != 'X' and not memo[ny][nx]:
                    memo[ny][nx] = True
                    q.append((ny, nx, cost + 1))

        return -1

    cost_1 = bfs('S','L')
    cost_2 = bfs('L','E')

    if cost_1 != -1 and cost_2 != -1:
        return cost_1 + cost_2

    return -1



print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
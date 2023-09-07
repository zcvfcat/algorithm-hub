from math import inf
from collections import deque


def solution(board):
    # init

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    h, w = len(board), len(board[0])
    memo = [[inf for _ in range(w)] for _ in range(h)]
    start, end = (), ()

    def in_boundary(ny,nx):
        return 0 <= ny < h and 0 <= nx < w

    for y in range(h):
        for x in range(w):
            if board[y][x] == 'R':
                start = (y, x)
            if board[y][x] == 'G':
                end = (y, x)
    # BFS
    start_y, start_x = start
    q = deque([(start_y, start_x, 0)])
    memo[start_y][start_x] = 0

    print(start)
    print(end)

    while q:
        y, x, cost = q.popleft()

        if (y, x) == end:
            return cost
        
        for dy, dx in direction:
            ny, nx = y, x

            while in_boundary(ny + dy, nx + dx) and board[ny + dy][nx + dx] != 'D':
                ny, nx= ny + dy, nx + dx

            if memo[ny][nx] > cost + 1:
                memo[ny][nx] = cost + 1
                q.append((ny, nx, cost + 1))
    return -1

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))

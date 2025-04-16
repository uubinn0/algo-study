'''
https://www.acmicpc.net/problem/4963


'''
import sys
sys.setrecursionlimit(10000)

result = list()
dyx = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def search(y, x, visited):
    for dy, dx in dyx:
        ny, nx = dy + y, dx + x

        # 범위 밖인 경우 다음으로
        if not(0 <= ny < Y and 0 <= nx < X): continue

        # 방문한 곳이라면
        if visited[ny][nx]: continue

        # 바다라면
        if BOARD[ny][nx] == 0: continue

        visited[ny][nx] = True
        search(ny, nx, visited)
    return


while True:
    X, Y = map(int, input().split())
    if X == 0 and Y == 0:
        break
    BOARD = [list(map(int, input().split())) for _ in range(Y)]
    visited = [[False] * X for _ in range(Y)]

    total_island = 0

    for y in range(Y):
        for x in range(X):
            if BOARD[y][x] == 1 and visited[y][x] == False:
                visited[y][x] = True
                search(y, x, visited)
                total_island += 1

    result.append(total_island)

for i in result:
    print(i)
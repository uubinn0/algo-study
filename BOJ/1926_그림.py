'''
https://www.acmicpc.net/problem/1926

testcase
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
'''

Y, X = map(int, input().split())
BOARD = [list(map(int, input().split())) for _ in range(Y)]
visited = [[False]*X for _ in range(Y)]

dyx = [(-1, 0), (0, 1), (1, 0), (0, -1)]

total_cnt = 0
max_size = 0


def search(y, x, pic_size, visited):
    size_result = 1

    for dy, dx in dyx:
        ny, nx = y + dy, x + dx

        # 새 좌표가 범위 밖이라면 다음으로
        if not (0 <= ny < Y and 0 <= nx < X): continue

        # 방문한 곳이라면
        if visited[ny][nx] == True: continue

        # 그림 영역이 아니라면
        if BOARD[ny][nx] == 0: continue

        visited[ny][nx] = True
        size_result += search(ny, nx, pic_size+1, visited)
        # print(f'size_result : {size_result}')

    return size_result


for y in range(Y):
    for x in range(X):
        if BOARD[y][x] == 1 and visited[y][x] == False:
            visited[y][x] = True
            current_size = search(y, x, 1, visited)
            total_cnt += 1
            max_size = max(max_size, current_size)

print(total_cnt)
print(max_size)
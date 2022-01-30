import copy

n, m = map(int, input().split())
a, b, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
result = 1

while True:
    t = copy.deepcopy(result)
    for _ in range(4):
        # 왼쪽으로 이동
        d -= 1

        if d < 0:
            d = 3

        visited[a][b] = 1

        # 방문하지 않은 곳 and 바다가 아닌 곳
        if d == 0 and visited[a - 1][b] == 0 and arr[a - 1][b] != 1:
            a -= 1
            result += 1
        elif d == 3 and visited[a][b - 1] == 0 and arr[a][b - 1] != 1:
            b -= 1
            result += 1
        elif d == 2 and visited[a + 1][b] == 0 and arr[a + 1][b] != 1:
            a += 1
            result += 1
        elif d == 1 and visited[a][b + 1] == 0 and arr[a][b + 1] != 1:
            b += 1
            result += 1

    if result == t:
        break

print(result)

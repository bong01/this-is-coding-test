loc = input()

row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
r = row.index(loc[0])
c = int(loc[1])

dx = [-2, -2, 2, 2, -1, -1, 1, 1]
dy = [-1, 1, -1, 1, -2, 2, -2, 2]

result = 0

for i in range(8):
    if (0 < r + dx[i] < 8 and 0 < c + dy[i] < 8) or (0 < r + dx[i] < 8 and 0 < c + dy[i] < 8):
        result += 1

print(result)

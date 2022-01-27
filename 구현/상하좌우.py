n = int(input())
command = list(input().split())

row = 1
col = 1
shift = {"U": -1, "D": 1, "L": -1, "R": 1}

for c in command:
    if c == "U" or c == "D":
        if not (row + shift[c] > n or row + shift[c] < 1):
            row += shift[c]
    else:
        if not (col + shift[c] > n or col + shift[c] < 1):
            col += shift[c]

print(row, col)

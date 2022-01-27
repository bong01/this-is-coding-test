n = int(input())

result = 0

for i in range(n + 1):
    if i in {3, 13, 23}:
        result += (60 * 60)
    else:
        result += (15 * 60) + (15 * 45)

print(result)

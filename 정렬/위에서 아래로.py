n = int(input())
arr = [int(input()) for _ in range(n)]

for num in sorted(arr, reverse=True):
    print(num, end=' ')

n, k = map(int, input().split())
arr1 = sorted(list(map(int, input().split())), reverse=True)
arr2 = sorted(list(map(int, input().split())), reverse=True)

for i in range(n - k, n):
    if arr1[i] < arr2[i - k]:
        arr1[i] = arr2[i - k]

print(sum(arr1))

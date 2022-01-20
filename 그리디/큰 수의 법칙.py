n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

sorted_arr = sorted(arr, reverse=True)
result = sorted_arr[0] * k * (m // k) + sorted_arr[1] * (m % k)

print(result)
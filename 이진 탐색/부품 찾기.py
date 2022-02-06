import sys

n = int(sys.stdin.readline().rstrip())
arr1 = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
arr2 = list(map(int, sys.stdin.readline().rstrip().split()))


def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)


for i in arr2:
    result = binary_search(arr1, i, 0, n-1)
    if result is None:
        print("no", end=' ')
    else:
        print("yes", end=' ')

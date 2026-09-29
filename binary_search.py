import sys
input = sys.stdin.readline


def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


if __name__ == "__main__":
    n, target = map(int, input().split())
    arr = list(map(int, input().split()))
    print(binary_search(arr, target))

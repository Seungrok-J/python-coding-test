import sys
input = sys.stdin.readline


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(*arr)


if __name__ == "__main__":
    solve()

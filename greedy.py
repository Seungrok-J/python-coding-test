import sys
input = sys.stdin.readline


def solve():
    n, k = map(int, input().split())
    coins = list(map(int, input().split()))
    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        count += k // coin
        k %= coin
    print(count)


if __name__ == "__main__":
    solve()

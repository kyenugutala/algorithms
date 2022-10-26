import sys

dp = [[-1 for j in range(100)]for i in range(100)]

def eggDropMaxFloor(n, k):
    # n--> eggs
    # k --> floors
    if (n == 1):  # if we have one egg then need to drop the egg from all the floors to check whether it breaks or not.
        return k
    if k == 0 or k == 1:
        return k  # if we have only one floor/zero floor then we have one option to check whether egg breaks or not.

    if dp[n][k] != -1:
        return dp[n][k]

    res = 0
    min = sys.maxsize
    for x in range(1,k + 1):
        res = 1+ max(eggDropMaxFloor(n - 1, x - 1), eggDropMaxFloor(n, k - x))
        if (res <min):
            min = res

    dp[n][k] = min
    return min


if __name__ == '__main__':
    print(eggDropMaxFloor(2, 7))

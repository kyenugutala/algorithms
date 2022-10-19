# Given a rod of length n inches and an array of prices that includes prices of all pieces of size smaller than n.
# Determine the maximum value obtainable by cutting up the rod and selling the pieces. For example,
# if the length of the rod is 8 and the values of different pieces are given as the following,
# then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)
#
# length   | 1   2   3   4   5   6   7   8
# --------------------------------------------
# price    | 1   5   8   9  10  17  17  20
# And if the prices are as following, then the maximum obtainable value is 24 (by cutting in eight pieces of length 1)
#
# length   | 1   2   3   4   5   6   7   8
# --------------------------------------------
# price    | 3   5   8   9  10  17  17  20


dp = [[0 for j in range(9)] for i in range(9)]


def getmaximumProfitByCuttingRod(prices, lengths, max_len, n):
    if max_len == 0 or n == 0:
        return 0

    if dp[n][max_len] !=0:
        return dp[n][max_len]

    if lengths[n - 1] <= max_len:
        dp[n][max_len] = max(prices[n - 1] + getmaximumProfitByCuttingRod(prices, lengths, max_len - lengths[n - 1],
                                                                          n),
                             getmaximumProfitByCuttingRod(prices, lengths, max_len, n - 1))
    else:
        dp[n][max_len] = getmaximumProfitByCuttingRod(prices, lengths, max_len, n - 1)

    return dp[n][max_len]


if __name__ == '__main__':
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    n = len(price)
    lengths = [0] * n
    for i in range(n):
        lengths[i] = i + 1

    print(getmaximumProfitByCuttingRod(price, lengths, n, n))

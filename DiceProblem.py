# n = 2, m = 6 , sum = 5
#
#     0 1 2 3 4 5
#  0  0 0 0 0 0 0
#  1  0 1 1 1 1 0
#  2  0 0 1 2 3 4
#  3  0 0 0 1 3 6
#
# if we have one dice then need to fill 1 for max faces like if teh dice has 4 faces then we need to fill till 4th column.
#     Sum (n,m,sum) = Sum(n-1,m,sum-1)+ sum(n-1,m,sum-2)+....+ sum(n-m,m,sum-m) =
# i =1 to m ∑ = sum (n-i,m,sum-i)

def getDiceThrowCount(m, n, x):
    dp = [[0 for j in range(x + 1)] for i in range(n + 1)]

    for j in range(min(m + 1, x + 1)):
        dp[1][j] = 1

    for i in range(2, n + 1):
        for j in range(1, x + 1):
            for k in range(1, min(m + 1, j)):
                dp[i][j] += dp[i - 1][j - k]

    return dp[-1][-1]


print(getDiceThrowCount(4, 3, 5))

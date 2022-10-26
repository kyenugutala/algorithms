# Given a gold mine of n*m dimensions.
# Each field in this mine contains a positive integer which is the amount of gold in tons.
# Initially the miner is at first column but can be at any row.
# He can move only (right->,right up /,right down\) that is from a given cell,
# the miner can move to the cell diagonally up towards the right or diagonally down towards
# the right. Find out maximum amount of gold he can collect.
#
# examples :
#
# Input : mat[][] = {{1, 3, 3},
#                    {2, 1, 4},
#                   {0, 6, 4}};
# Output : 12
# {(1,0)->(2,1)->(1,2)}
#
# Input: mat[][] = { {1, 3, 1, 5},
#                    {2, 2, 4, 1},
#                    {5, 0, 2, 3},
#                    {0, 6, 1, 2}};
# Output : 16
# (2,0) -> (1,1) -> (1,2) -> (0,3) OR
# (2,0) -> (3,1) -> (2,2) -> (2,3)
#
# Input : mat[][] = {{10, 33, 13, 15},
#                   {22, 21, 04, 1},
#                   {5, 0, 2, 3},
#                   {0, 6, 14, 2}};
# Output : 83

def getMaxGoldMine(input, i , j,row,column,dp):

    if not(i < row and i >=0 and j < column and j>=0):
        return 0

    if j == column-1:
        return input[i][j]

    if dp[i][j] != 0:
        return dp[i][j]


    for i in range(row):
        dp[i][j] = input[i][j] + max(getMaxGoldMine(input,i, j+1,row,column,dp),
                                getMaxGoldMine(input, i+1,j+1,row,column,dp),
                                getMaxGoldMine(input,i-1,j+1,row,column,dp))

    return dp[i][j]


if __name__ =='__main__':
    # input = [[1,3,3],[2,1,4],[0,6,4]]
    #input = [[1, 3, 1, 5],[2, 2, 4, 1],[5, 0, 2, 3],[0, 6, 1, 2]]
    input = [[10, 33, 13, 15],
             [22, 21, 4, 1],
             [5, 0, 2, 3],
             [0, 6, 14, 2]]
    length = len(input[0])
    dp = [[0 for j in range(length)] for i in range(length)]
    getMaxGoldMine(input,0,0,length,length,dp)
    max_Value = 0
    for i in range(length):
        max_Value = max(max_Value,dp[i][0])

    print(max_Value)




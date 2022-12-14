# Given a ā2 x nā board and tiles of size ā2 x 1ā,
# count the number of ways to tile the given board using the 2 x 1 tiles.
# A tile can either be placed horizontally i.e., as a 1 x 2 tile or vertically i.e.,
# as 2 x 1 tile.
#
# Explanation:
#
# For a 2 x 4 board, there are 5 ways
#
# All 4 vertical (1 way)
# All 4 horizontal (1 way)
# 2 vertical and 2 horizontal (3 ways)
# Input: n = 3
#
# Output: 3
#
# Explanation:
#
# We need 3 tiles to tile the board of size  2 x 3.
#
# We can tile the board using following ways
#
# Place all 3 tiles vertically.

def getNofWaysToplacetheTiles(n):
    if n==1 or n==2:
        return n;

    return getNofWaysToplacetheTiles(n-1)+ getNofWaysToplacetheTiles(n-2);

print(getNofWaysToplacetheTiles(4))
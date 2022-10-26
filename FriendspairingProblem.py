# Input  : n = 3
# Output : 4
# Explanation:
# {1}, {2}, {3} : all single
# {1}, {2, 3} : 2 and 3 paired but 1 is single.
# {1, 2}, {3} : 1 and 2 are paired but 3 is single.
# {1, 3}, {2} : 1 and 3 are paired but 2 is single.
# Note that {1, 2} and {2, 1} are considered same.
# Recursive Algo
# f(n) = ways n people can remain single
#        or pair up.
#
# For n-th person there are two choices:
# 1) n-th person remains single, so only 1 way so  we recur
#    for remaining i.e f(n - 1)   or you can say 1*f(n-1)
# 2) n-th person pairs up with any of the
#    remaining n - 1 persons. So apart from the 2 people forming a pair for remaining n-2 persons we We get (n - 1) * f(n - 2) ways
#
# Therefore we can recursively write f(n) as:
# f(n) = f(n - 1) + (n - 1) * f(n - 2)

dp = [0 for i in range(100)]

def getFriendspairingVal( n):

    if n<=2 :
        return n

    if dp[n] != 0:
        return dp[n]

    dp[n] = 1*getFriendspairingVal(n-1)+ (n-1)*getFriendspairingVal(n-2)

    return dp[n]

if __name__=='__main__':

    print(getFriendspairingVal(3))



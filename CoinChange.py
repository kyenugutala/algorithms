def getNoOfPossibleToGetCoinChange(coins,sum):
    df = [0 for x in range(sum+1)]
    df[0] = 1

    for i in range(len(coins)):
        for j in range(coins[i], sum+1):
            df[j]+=df[j-coins[i]]

    return df[sum]

if __name__=='__main__':
    coins = [1,2,3]
    sum = 15
    print(getNoOfPossibleToGetCoinChange(coins,sum))

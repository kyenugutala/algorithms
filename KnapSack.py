import sys


def getmaximumTotalvalueFromKnpsack(value, weight, w):
    n = len(value)
    df = [[0 for j in range(w + 1)] for i in range(n + 1)]


    for x in range(n + 1):
        for y in range(w + 1):
            if x == 0 or y == 0:
                df[x][y] = 0
            elif weight[x - 1] <= y:
                df[x][y] = max(value[x - 1] + df[x - 1][y - weight[x - 1]],df[x-1][y])
            else:
                df[x][y] = df[x - 1][y]

    return df[n][w]


if __name__ == '__main__':

    value = [60, 100, 120]
    weight = [1, 2, 3]
    w = 5
    print(getmaximumTotalvalueFromKnpsack(value, weight, w))

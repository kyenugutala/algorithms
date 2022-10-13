# cutting the rope at every 3 meteres will give the max product val
def getMaxiumRopeCutVal(ropeLength):
    if ropeLength == 2 or ropeLength == 3:
        return ropeLength - 1

    res = 1
    while (ropeLength > 4):
        res = res * 3
        ropeLength = ropeLength - 3

    return res * ropeLength


if __name__ == '__main__':
    print(getMaxiumRopeCutVal(10))

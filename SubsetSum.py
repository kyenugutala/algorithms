# set[] = {3, 4, 5, 2}
# sum = 9
# (x, y) = 'x' is the
# left
# number
# of
# elements,
# 'y' is the
# required
# sum
#
# (4, 9)
# {True}
# / \
#     (3, 6)(3, 9)
#
# /     \ / \
#     (2, 2)(2, 6)(2, 5)(2, 9)
# {True}
# / \
#     (1, -3)(1, 2)
# {False}
# {True}
# / \
#     (0, 0)(0, 2)
# {True}
# {False}


def isSubsetSumExists(input, startIndex, endIndex, sum):
    if startIndex > endIndex:
        return False
    elif startIndex == endIndex and input[startIndex] != sum:
        return False

    nextIndex = startIndex + 1
    if input[startIndex] == sum:
        return True
    elif input[startIndex] <= sum:
        return isSubsetSumExists(input, nextIndex, endIndex, sum - input[startIndex]) or isSubsetSumExists(input,
                                                                                                           nextIndex,
                                                                                                           endIndex,
                                                                                                           sum)
    else:
        return isSubsetSumExists(input,
                                 nextIndex,
                                 endIndex,
                                 sum)


if __name__ == '__main__':
    input = [3, 34, 4, 12, 5, 2]
    sum = 26
    print(isSubsetSumExists(input, 0, len(input) - 1, sum))

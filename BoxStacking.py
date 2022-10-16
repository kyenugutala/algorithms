class Box:
    def __init__(self, h, w, d):
        self.h = h
        self.w = w
        self.d = d

    def __lt__(self, other):
        return self.w * self.d < other.w * other.d


def getMaximumBoxStackingLength(boxArray, n):
    rt = [Box(0, 0, 0) for b in range(n * 3)]

    index = 0
    for i in range(n):
        rt[index].h = boxArray[i].h
        rt[index].w = max(boxArray[i].w, boxArray[i].d)
        rt[index].d = min(boxArray[i].w, boxArray[i].d)

        index = index + 1;

        rt[index].h = boxArray[i].w
        rt[index].w = max(boxArray[i].h, boxArray[i].d)
        rt[index].d = min(boxArray[i].h, boxArray[i].d)

        index = index + 1

        rt[index].h = boxArray[i].d
        rt[index].w = max(boxArray[i].h, boxArray[i].w)
        rt[index].d = min(boxArray[i].h, boxArray[i].w)

        index = index + 1
    rt.sort(reverse=True)

    n = n * 3
    msh = [0] * n

    for i in range(n):
        msh[i] = rt[i].h

    # 5   5
    # 4   4
    # 6   11
    # 8
    for i in range(1, n):
        for j in range(0, i):
            if rt[i].w < rt[j].w and rt[i].d < rt[j].d:
                if msh[i] < msh[j] + rt[i].h:
                    msh[i] = msh[j] + rt[i].h

    maximum = -1
    for k in range(n):
        maximum = max(maximum, msh[i])

    return maximum


# Driver Code
# always Box Length should be greater than the depth.
# So every Box object has three posibilities.
# order all the boxes in desending order.
# create a another array with box heights.
# iterate from Box from that position to up . i.e 1 index to zero index.
# if the width*depth is lesser than previous position Box then sum the msh[i]+ rt[j]
# if msh[i] < msh[i]+ rt[j] then store it in msh[i] and finally iterate all the result heights and return heighest one.
if __name__ == "__main__":
    arr = [Box(4, 6, 7), Box(1, 2, 3),
           Box(4, 5, 6), Box(10, 12, 32)]
    n = len(arr)
    print("The maximum possible height of stack is",
          getMaximumBoxStackingLength(arr, n))

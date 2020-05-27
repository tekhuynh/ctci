def maxheight(boxes):
    memo = dict()
    maxheight2(boxes, memo)
    print(memo)
    return max(memo.values())

def maxheight2(boxes, memo):
    if not boxes:
        return 0
    if len(boxes) == 1:
        return boxes[0][1]

    currmax = 0

    for box in boxes:
        if not box in memo:
            smaller = [x for x in boxes if bigger(box, x)]
            memo[box] = box[1] + maxheight2(smaller, memo)
        if memo[box] > currmax:
            currmax = memo[box]

    return currmax

def bigger(big, small):
    if big[0] <= small[0]:
        return False
    if big[1] <= small[1]:
        return False
    if big[2] <= small[2]:
        return False
    return True

print(maxheight([(1,1,1), (2,2,2), (3,3,3), (4,4,4), (1,2,3), (2,3,4), (3,4,5), (4,5,6)]))
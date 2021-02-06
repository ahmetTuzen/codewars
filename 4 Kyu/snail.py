def snail(snail_map):
    result = []

    row = len(snail_map)
    col = len(snail_map[0])
    tot = row * col

    movement = "r"
    moveCount = 0

    while True:
        if movement is "r":
            if moveCount == 0:
                for i in snail_map[int(moveCount / 4)]:
                    result.append(i)
            else:
                for i in snail_map[int(moveCount / 4)][int(moveCount / 4):-int(moveCount / 4)]:
                    result.append(i)
            movement = "d"
            moveCount += 1
        if len(result) == tot:
            break
        if movement is "d":
            offset = int((moveCount + 3) / 4)
            lastElement = int((moveCount - 1) / 4)
            for i in range(offset, row-lastElement):
                result.append(snail_map[i][col - offset])
            movement = "l"
            moveCount += 1
        if len(result) == tot:
            break
        if movement is "l":
            offset = int((moveCount + 2) / 4)
            lastElement = int((moveCount - 2) / 4)
            for i in range(col-offset, lastElement, -1):
                result.append(snail_map[row - lastElement - 1][i - 1])
            movement = "u"
            moveCount += 1
        if len(result) == tot:
            break
        if movement is "u":
            offset = int((moveCount + 1) / 4)
            lastElement = int((moveCount - 3) / 4)
            for i in range(row-offset, offset, -1):
                result.append(snail_map[i-1][offset-1])
            movement = "r"
            moveCount += 1
        if len(result) == tot:
            break

    return result

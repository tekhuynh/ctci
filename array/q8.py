def q8(m):
    nrows = len(m)
    ncols = len(m[0])

    zrow = [0] * nrows
    zcol = [0] * ncols

    for i in range(nrows):
        for j in range(ncols):
            if m[i][j] == 0:
                zrow[i] += 1
                zcol[j] += 1

    for nzeros in zrow:
        if nzeros != 0 or nzeros != nrows:
            return False
    for nzeros in zcol:
        if nzeros != 0 or nzeros != ncols:
            return False

    return True

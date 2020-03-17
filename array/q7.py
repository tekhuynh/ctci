def rotate90(m):
    dim = len(m[0])

    for i in range(dim):
        for j in range(i):
            m[i][j], m[j][i] = m[j][i], m[i][j]
    
    for i in range(dim):
        for j in range(int(dim/2)):
            m[i][j], m[i][dim-j-1] = m[i][dim-j-1], m[i][j]
    
    return m


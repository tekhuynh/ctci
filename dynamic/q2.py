class Position:
    def __init__(self, r, c, p):
        self.row = r
        self.col = c
        self.parent = p

def findpath(grid, rows, columns):
    visited = [[False] * columns for i in range(rows)]
    return findpath2(grid, rows, columns, Position(rows-1,columns-1,None), visited)

def findpath2(grid, rows, columns, position, visited):
    print("(%d, %d)" % (position.row, position.col))
    if position is None:
        return None
    if position.row == 0 and position.col == 0:
        path = []
        while not position is None:
            path.append("(%d, %d)" % (position.row, position.col))
            position = position.parent
        return path
    
    if not grid[position.row][position.col]:
        return None

    if visited[position.row][position.col]:
        return None
    
    if position.row < 0 or position.col < 0:
        return None

    visited[position.row][position.col] = True
    up = Position(position.row - 1, position.col, position)
    left = Position(position.row, position.col - 1, position)

    leftpath = findpath2(grid, rows, columns, left, visited)
    if leftpath:
        return leftpath
    uppath = findpath2(grid, rows, columns, up, visited)
    if uppath:
        return uppath

    
    return None

p = [[True] * 10 for i in range(10)]
p[8][1] = False
p[9][0] = False
print(findpath(p, 10, 10))
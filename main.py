 
def isCorrectRect(points):
    if not isinstance(points, list) or len(points) != 2:
        return False

    bottomleft, topright = points

    if not (isinstance(bottomleft, tuple) and isinstance(topright, tuple)):
        return False

    if len(bottomleft) != 2 or len(topright) != 2:
        return False

    if not all(isinstance(coord, (int, float)) for coord in bottomleft + topright):
        return False

    return bottomleft[0] < topright[0] and bottomleft[1] < topright[1]
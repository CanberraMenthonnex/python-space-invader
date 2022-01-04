def Collision(x, y , i, j, distance):
    if ((((x - i )**2) + ((y-j)**2) )**0.5) < distance:
        return True
    return False
    
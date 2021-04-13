import math 

def f (x: float) -> float:
    if (x <= math.sqrt(2.0)):
        return -math.pow(x - math.sqrt(2), 2)
    return math.pow(x - math.sqrt(2), 2)

exactValue = 15 - (31 * math.sqrt(2)) / 3
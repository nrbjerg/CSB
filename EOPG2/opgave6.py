G = 6.67e-11
m = 2.7e10

def explicitTrapezMethod (r: float, h: float, k1: float, k2: float) -> float:
    return r + h/2 * (k1 + k2)

def methods (r: float, h: float, f: function):
    k1 = 
    

    

def f (r):
    if (r >= 0.1):
        return -G*m / r**2
    else: raise ValueError("Invalid radius")
    
if __name__ == "__main__"
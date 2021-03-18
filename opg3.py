from numpy import log, cos, sin, tan, sqrt, zeros, linspace, sum, pi

if __name__ == "__main__":
    a, b = 0, 1
    # f = lambda x: cos(x)
    # f = lambda x: sqrt(x)
    f = lambda x: log(x) if (x != 0) else 0
    h = b / 4
    I = 8*h / 3 * f(h) - 4 * h/3 * f(2*h) + 8*h/3 * f(3*h)
    print(f"intergal: {I}")

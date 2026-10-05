def f(x):
    return x**3 - x - 2
def df(x):
    return 3*x**2 - 1

#Bisection Method
def bisection(accuracy):

    xl = 1
    xu = 2
    xr_old = None
    i = 0

    while True:
        i += 1

        xr = (xl + xu) / 2

        if xr_old is None:
            Er = 0
        else:
            Er = abs((xr - xr_old) / xr) * 100

        if xr_old is not None and Er < accuracy:
            return i, xr

        if f(xl) * f(xr) < 0:
            xu = xr
        else:
            xl = xr

        xr_old = xr



# 2. False Position Method
def false_position(accuracy):

    xl = 1
    xu = 2
    xr_old = None
    i = 0

    while True:
        i += 1

        xr = (xl * f(xu) - xu * f(xl)) / (f(xu) - f(xl))

        if xr_old is None:
            Er = 0
        else:
            Er = abs((xr - xr_old) / xr) * 100

        if xr_old is not None and Er < accuracy:
            return i, xr

        if f(xl) * f(xr) < 0:
            xu = xr
        else:
            xl = xr

        xr_old = xr



# 3. Newton-Raphson Method
def newton_raphson(accuracy):

    x_old = 1.5
    i = 0

    while True:
        i += 1

        x_new = x_old - f(x_old) / df(x_old)

        Er = abs((x_new - x_old) / x_new) * 100

        if Er < accuracy:
            return i, x_new

        x_old = x_new



# Main Program
accuracy = float(input("Enter required accuracy (%): "))

b_i, b_root = bisection(accuracy)
fp_i, fp_root = false_position(accuracy)
n_i, n_root = newton_raphson(accuracy)

print("\nApproach\tIteration\tFinal Root")
print("Bisection\t", b_i, "\t\t", b_root)
print("False Position\t", fp_i, "\t\t", fp_root)
print("Newton-Raphson\t", n_i, "\t\t", n_root)
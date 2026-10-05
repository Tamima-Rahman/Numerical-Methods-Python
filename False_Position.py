def f(x):
    return x**2 - 7

xl = float(input("Enter lower limit: "))
xu = float(input("Enter upper limit: "))
xr_old = None
i = 0
print("\nIter\t xl\t\t xu\t\t xr\t\t Ea\t\t Er(%)\t\t Range")

while True:
    xr = (xl * f(xu) - xu * f(xl)) / (f(xu) - f(xl))

    i = i + 1
    if xr_old is None:
        Ea = 0
        Er = 0
    else:
        Ea = abs(xr - xr_old)
        Er = abs((xr - xr_old) / xr) * 100

    if f(xl) * f(xr) < 0:
        range_change ="c -> b"
    else:
        range_change ="c -> a"

    print(f"{i}\t{xl:.6f}\t{xu:.6f}\t{xr:.6f}\t{Ea:.6f}\t{Er:.6f}\t{range_change}")

    if Er < 0.01 and xr_old is not None:
        break
    if f(xl) * f(xr) < 0:
        xu = xr
    else:
        xl = xr

    xr_old = xr
print("\nRoot =", xr)
print("Number of iterations =", i)
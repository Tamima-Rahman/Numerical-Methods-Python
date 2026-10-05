def f(x):
    return eval(function)

function = input("Enter f(x): ")
x0 = float(input("Enter first initial value: "))
x1 = float(input("Enter second initial value: "))
n = int(input("Enter significant figures: "))
Es = 0.5 * (10 ** (2 - n))
print("\nEs =", Es)

print("\nIter\tx0\t\t x1\t\t x_new\t\t Ea\t\t Er(%)")
i = 0
while True:
    i+=1
    x_new = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
    Ea = abs(x_new - x1)
    if x_new == 0:
        Er = 0
    else:
        Er = abs((x_new - x1) / x_new) * 100

    print(f"{i}\t{x0:.6f}\t{x1:.6f}\t{x_new:.6f}\t{Ea:.6f}\t{Er:.6f}")

    if i > 1 and Er < Es:
        break
    x0 = x1
    x1 = x_new
print("\nApproximate Root =", x_new)
print("f(root) =", f(x_new))
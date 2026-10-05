def f(x):
    return eval(function_f)
def g1(x):
    return eval(function_g1)
def g2(x):
    return eval(function_g2)
def dg1(x):
    return eval(function_dg1)
def dg2(x):
    return eval(function_dg2)

function_f = input("Enter f(x): ")
function_g1 = input("Enter g1(x): ")
function_g2 = input("Enter g2(x): ")
function_dg1 = input("Enter dg1(x): ")
function_dg2 = input("Enter dg2(x): ")


x_old = float(input("Enter initial value: "))
n = int(input("Enter significant figures: "))
Es = 0.5 * (10 ** (2 - n))
print("\nEs =", Es, "%")

if abs(dg1(x_old)) < 1:
    print("\ng1(x) satisfies the convergence")
    g = g1

elif abs(dg2(x_old)) < 1:
    print("\ng2(x) satisfies the convergence")
    g = g2
else:
    print("\nNeither g1(x) nor g2(x) satisfies the convergence")
    g = None

if g is not None:

    i = 0
    print("\nIter\t x_old\t\t x_new\t\t Ea\t\t Er(%)")

    while True:
        x_new = g(x_old)
        if i == 0:
            Ea = 0
            Er = 0
        else:
            Ea = abs(x_new - x_old)
            Er = abs((x_new - x_old) / x_new) * 100

        print(f"{i+1}\t{x_old:.6f}\t{x_new:.6f}\t{Ea:.6f}\t{Er:.6f}")

        if i > 0 and Er <= Es:
            break

        x_old = x_new
        i += 1

    print("\nRoot approx:", x_new)
    print("Check f(root):", f(x_new))
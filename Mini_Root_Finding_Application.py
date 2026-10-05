print("Mini Root Finding Application")
print("\n1.Bisection")
print("\n2.Fixed Point")
print("\n3.False Position")
print("\n4.Newton Raphson")
print("\n5.Secant Method")

choice = int(input())
def f(x):
    return eval(function)
function = input()

if choice == 1:

    a = float(input())
    b = float(input())
    mid_old = None
    accuracy = float(input())
    print("\nIter\ta\t\tb\t\tmid\t\tEa\t\tEr")
    i = 0

    while True:

        i += 1
        mid = (a + b) / 2
        if mid_old is None:
            Ea = 0
            Er = 0
        else:
            Ea = abs(mid - mid_old)

            if mid == 0:
                Er = 0
            else:
                Er = abs((mid - mid_old) / mid) * 100

        print(f"{i}\t{a:.3f}\t{b:.3f}\t{mid:.3f}\t{Ea:.3f}\t{Er:.3f}")

        if f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid

        if mid_old is not None and Er < accuracy:
            break

        mid_old = mid

    print("Root =", mid)


elif choice == 2:

    def g1(x):
        return eval(function_g1)

    def d1(x):
        return eval(function_d1)

    def g2(x):
        return eval(function_g2)

    def d2(x):
        return eval(function_d2)

    function_g1 = input()
    function_g2 = input()
    function_d1 = input()
    function_d2 = input()

    x0 = float(input())
    accuracy = float(input())

    if abs(d1(x0)) < 1:
        g = g1

    elif abs(d2(x0)) < 1:
        g = g2

    else:
        g = None

    if g is not None:

        i = 0

        print("\nIter\t x0\t\t x_new\t\t Ea\t\t Er")

        while True:

            i += 1

            x_new = g(x0)

            if i == 1:
                Ea = 0
                Er = 0
            else:
                Ea = abs(x_new - x0)

                if x_new == 0:
                    Er = 0
                else:
                    Er = abs((x_new - x0) / x_new) * 100

            print(f"{i}\t{x0:.3f}\t{x_new:.3f}\t{Ea:.3f}\t{Er:.3f}")

            if i > 1 and Er < accuracy:
                break

            x0 = x_new

        print("Root =", x_new)

    else:
        print("Neither g1 nor g2 satisfies convergence condition")


elif choice == 3:

    a = float(input())
    b = float(input())
    accuracy = float(input())
    i = 0
    c_old = None

    print("\nIter\t a\t\t b\t\t c\t\t Ea\t\t Er")

    while True:

        i += 1
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        if c_old is None:
            Ea = 0
            Er = 0
        else:
            Ea = abs(c - c_old)

            if c == 0:
                Er = 0
            else:
                Er = abs((c - c_old) / c) * 100

        print(f"{i}\t{a:.3f}\t{b:.3f}\t{c:.3f}\t{Ea:.3f}\t{Er:.3f}")

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        if c_old is not None and Er < accuracy:
            break

        c_old = c

    print("Root =", c)


elif choice == 4:

    def d(x):
        return eval(function_d)

    function_d = input()

    x0 = float(input())
    accuracy = float(input())

    print("\nIter\t x\t\t Ea\t\t Er")

    i = 0

    while True:

        i += 1
        x_new = x0 - f(x0) / d(x0)
        Ea = abs(x_new - x0)

        if x_new == 0:
            Er = 0
        else:
            Er = abs((x_new - x0) / x_new) * 100

        print(f"{i}\t{x_new:.3f}\t{Ea:.3f}\t{Er:.3f}")

        if Er < accuracy:
            break

        x0 = x_new

    print("Root =", x_new)


elif choice == 5:

    x0 = float(input())
    x1 = float(input())
    accuracy = float(input())

    print("\nIter\t x0\t\t x1\t\t x_new\t\t Ea\t\t Er")

    i = 0

    while True:

        i += 1
        x_new = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        Ea = abs(x_new - x1)

        if x_new == 0:
            Er = 0
        else:
            Er = abs((x_new - x1) / x_new) * 100

        print(f"{i}\t{x0:.3f}\t{x1:.3f}\t{x_new:.3f}\t{Ea:.3f}\t{Er:.3f}")

        if Er < accuracy:
            break

        x0 = x1
        x1 = x_new

    print("Root =", x_new)

else:
    print("Invalid")
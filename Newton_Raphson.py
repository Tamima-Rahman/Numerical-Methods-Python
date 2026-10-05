def f(x):
    return eval(function)

def df(x):
    return eval(derivative)

function = input("Enter f(x): ")
derivative = input("Enter f'(x): ")
x_old = float(input("Enter initial value: "))
decimal_places = int(input("Enter required decimal places: "))

print("\nIter\tx\t\tEa\t\tEr(%)")

i = 0
while True:
    i +=1
    x_new = x_old - f(x_old) / df(x_old)
    Ea = abs(x_new - x_old)
    Er = abs((x_new - x_old) / x_new) * 100
    print(f"{i}\t{x_new:.6f}\t{Ea:.6f}\t{Er:.6f}")

    if Ea < 0.0001:
        break
    x_old = x_new

print("\nApproximate Root =", round(x_new, decimal_places))
print("f(root) =", f(x_new))
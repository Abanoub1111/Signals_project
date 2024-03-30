import cmath

def f(x):
    functions = [cmath.cos(x), cmath.sin(x), cmath.tan(x), cmath.exp(x), cmath.log(x), cmath.acos(x), cmath.asin(x)]
    return cmath.cos(x) + 6j * cmath.sin(2*x)*cmath.exp(1j * w * x)


def integral(a, b, N):
    delta_x = (b - a) / N
    integral_sum = 0

    for i in range(1, N+1):
        x_i = a + (i-1) * delta_x
        integral_sum += f(x_i) *delta_x

    return integral_sum

a = int(input('Enter the Lower limit: '))
b = int(input('Enter the Upper limit: '))
N = 1000
w = 1

result = integral(a, b, N)

print(f"Approximate integral value: {result:.6f}")

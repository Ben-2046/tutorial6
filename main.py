def f(x):
    return(-x**2 + 3*x - 2)

h=0.10
a=1
b=2
print("f(x) = -x^2 + 3x - 2 from a=1 to b=2")
x = a
while x < b+h/2:
    print("When x =",x,"=> f(x) =", f(x))
    x += h

first = f(a)
last = f(b)
x = a+h
ms = 0
while x < b:
    ms += f(x)
    x += h

ApproxValue = (h/2)*(first + ms*2 + last)
TrueValue = 1/6

print("Example of Trapezium Rule Values")
print("First Height:", first)
print("Last Height:", last)
print("Middle Sum:", ms)
print("Integration is approximately", ApproxValue)
print("True value of integration is 1/6")

error = 100*(TrueValue-ApproxValue)/TrueValue
print("Therefore the error is ",error,"%")

quit()


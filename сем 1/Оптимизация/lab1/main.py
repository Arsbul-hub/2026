from scipy.special import jv, yv
from numpy import cos, sin
import bisectial
import iterational
import newton
# Основа
func1 = lambda x: jv(0, x)
dfunc1 = lambda x: -jv(1, x)
func2 = lambda x: jv(1, x)
dfunc2 = lambda x: jv(0, x) - jv(1, x) / x
func3 = lambda x: yv(0, x)
dfunc3 = lambda x: -yv(1, x)
func4 = lambda x: yv(1, x)
dfunc4 = lambda x: yv(0, x) - yv(1, x) / x
interval1 = bisectial.find_interval(func1, 0.1, 0.1)
interval2 = bisectial.find_interval(func1, interval1[1] + 0.1, 0.1)
interval3 = bisectial.find_interval(func2, 0.1, 0.1)
interval4 = bisectial.find_interval(func2, interval3[1] + 0.1, 0.1)
interval5 = bisectial.find_interval(func3, 0.1, 0.1)
interval6 = bisectial.find_interval(func3, interval5[1] + 0.1, 0.1)
interval7 = bisectial.find_interval(func4, 0.1, 0.1)
interval8 = bisectial.find_interval(func4, interval7[1] + 0.1, 0.1)

print("Bisectial")
print("jv(0, x)")
j0x1 = bisectial.find_solutions(func1, interval1)
print(j0x1)
j0x2 = bisectial.find_solutions(func1, interval2)
print(j0x2)
print("jv(1, x)")
j1x1 = bisectial.find_solutions(func2, interval3)
print(j1x1)
j1x2 = bisectial.find_solutions(func2, interval4)
print(j1x2)
print("yv(0, x)")
y0x1 = bisectial.find_solutions(func3, interval5)
print(y0x1)
y0x2 = bisectial.find_solutions(func3, interval6)
print(y0x1)
print("yv(1, x)")
y1x1 = bisectial.find_solutions(func4, interval7)
print(y1x1)
y1x2 = bisectial.find_solutions(func4, interval8)
print(y1x2)
bisectial.show_plot()

print("Iterational")
print("jv(0, x)")
M1 = dfunc1(j0x1)
M2 = dfunc1(j0x2)
M3 = dfunc2(j1x1)
M4 = dfunc2(j1x2)
M5 = dfunc3(y0x1)
M6 = dfunc3(y0x2)
M7 = dfunc4(y1x1)
M8 = dfunc4(y1x2)
ifunc1 = lambda x: x - func1(x) / M1
ifunc2 = lambda x: x - func1(x) / M2
ifunc3 = lambda x: x - func2(x) / M3
ifunc4 = lambda x: x - func2(x) / M4
ifunc5 = lambda x: x - func3(x) / M5
ifunc6 = lambda x: x - func3(x) / M6
ifunc7 = lambda x: x - func4(x) / M7
ifunc8 = lambda x: x - func4(x) / M8
print(iterational.find_solutions(func1, ifunc1, interval1))
print(iterational.find_solutions(func1, ifunc2, interval2))
print("jv(1, x)")
print(iterational.find_solutions(func2, ifunc3, interval3))
print(iterational.find_solutions(func2, ifunc4, interval4))
print("yv(0, x)")
print(iterational.find_solutions(func3, ifunc5, interval5))
print(iterational.find_solutions(func3, ifunc6, interval6))
print("yv(1, x)")
print(iterational.find_solutions(func4, ifunc7, interval7))
print(iterational.find_solutions(func4, ifunc8, interval8))
iterational.show_plot()
print("Newton")
print("jv(0, x)")
print(newton.find_solutions(func1, dfunc1, interval1))
print(newton.find_solutions(func1, dfunc1, interval2))
print("jv(1, x)")
print(newton.find_solutions(func2, dfunc2, interval3))
print(newton.find_solutions(func2, dfunc2, interval4))
print("yv(0, x)")
print(newton.find_solutions(func3, dfunc3, interval5))
print(newton.find_solutions(func3, dfunc3, interval6))
print("yv(1, x)")
print(newton.find_solutions(func4, dfunc4, interval7))
print(newton.find_solutions(func4, dfunc4, interval8))
newton.show_plot()
# Тесты
print("TESTS")

print("Bisectial x**2 - 2")

func1 = lambda x: x**2 - 2
interval_negative = bisectial.find_interval(func1, -10, 0.1)
print(bisectial.find_solutions(func1, interval_negative))
interval_positive = bisectial.find_interval(func1, 0, 0.1)
print(bisectial.find_solutions(func1, interval_positive))

func1 = lambda x: cos(x) - x
interval_positive = bisectial.find_interval(func1, 0, 0.1)
print(bisectial.find_solutions(func1, interval_positive))

print("Iterational x**2 - 2")
func1 = lambda x: x**2 - 2
gx = lambda x: x - func1(x) / (-2 * (2**0.5))
interval_negative = iterational.find_interval(func1, -2, 0.1)
print(iterational.find_solutions(func1, gx, interval_negative))
gx = lambda x: x - func1(x) / (2 * (2**0.5))
interval_positive = iterational.find_interval(func1, 0, 0.1)
print(iterational.find_solutions(func1, gx, interval_positive))
#
print("Iterational cos(x) = x")
func1 = lambda x: cos(x) - x
gx = lambda x: cos(x)
interval_positive = iterational.find_interval(func1, 0, 0.1)
print(iterational.find_solutions(func1, gx, interval_positive))

print("newton x ** 2 - 2")
func1 = lambda x: x**2 - 2
df = lambda x: 2 * x
interval_negative = newton.find_interval(func1, -2, 0.1)
print(newton.find_solutions(func1, df, interval_negative))
interval_positive = newton.find_interval(func1, 0.1, 0.1)
print(newton.find_solutions(func1, df, interval_positive))

print("newton cos(x)")
func1 = lambda x: cos(x) - x
df = lambda x: -sin(x) - 1
interval_positive = newton.find_interval(func1, 0.1, 0.1)
print(newton.find_solutions(func1, df, interval_positive))

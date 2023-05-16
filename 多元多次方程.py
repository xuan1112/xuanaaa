from sympy import *
from sympy import symbols, Poly, linsolve

# # 定义方程
# equation = "2*x**4 - 3*x**3 + 4*x**2 - 5*x + 6"
#
# # 将方程转换为多项式对象
# poly = Poly(equation)
#
# # 求解方程
# solutions = solve(poly)
#
# # 输出结果
# print("方程的解为：", solutions)
#
#
#
#
# # 定义符号变量
# x, y = symbols('x y')
#
# # 输入二元多项式方程
# equation = "2*x**4 - 3*y**4   4*x**2*y**2 - 6"
#
# # 将输入的字符串转换为SymPy中的多项式对象
# poly = Poly(equation)
#
# # 提取出二元多项式方程中的系数
# coefficients = poly.coeffs()
#
# # 使用linsolve函数解方程组
# solutions = linsolve(coefficients, [x, y])
#
# # 输出解
# print("方程的解为：", solutions)
#
#
#
# # 定义三个符号变量
# x, y, z = symbols('x y z')
#
# # 输入三元多项式方程
# equation = '2*x**4 - 3*y**4 + 4*z**3 - 5*x*y*z + 6'
#
# # 将输入的字符串转换为SymPy中的多项式对象
# poly = Poly(equation)
#
# # 提取出三元多项式方程中的系数
# coefficients = poly.coeffs()
#
# # 使用linsolve函数解方程组
# solutions = linsolve(coefficients, [x, y, z])
#
# # 输出解
# print("方程的解为：", solutions)

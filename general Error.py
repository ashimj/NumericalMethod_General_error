import sympy as sym
# setting symbols
x, y, z = sym.symbols('x y z')
# setting function
u = (5 * x * y ** 2) / (z ** 3)
# calculating partial derivatives
partial_x = sym.diff(u, x)
partial_y = sym.diff(u, y)
partial_z = sym.diff(u, z)

# calculating partial differentiation values
value_par_x = float(partial_x.subs({x: 1, y: 1, z: 1}))
value_par_y = float(partial_y.subs({x: 1, y: 1, z: 1}))
value_par_z = float(partial_z.subs({x: 1, y: 1, z: 1}))
value_u = abs(float(u.subs({x: 1, y: 1, z: 1})))

# setting given del values
del_x = 0.001
del_y = 0.001
del_z = 0.001

# calculating maximum error
del_u = abs(value_par_x*del_x)+abs(value_par_y*del_y)+abs(value_par_z*del_z)

# output
print("Maximum error = ", del_u)
print("Relative error = ", del_u/value_u)
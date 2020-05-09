import cmath
comp=complex(input())

phase = cmath.phase(comp)
    
x = comp.real
y = comp.imag

print("x : ",x)
print("y : ",y)

r = cmath.sqrt(x**x + y**y)
r = r.real

print("Using normals method : ",r)

print("Using abs method : ",abs(comp)) # Similar to r

print("phase : ",phase)

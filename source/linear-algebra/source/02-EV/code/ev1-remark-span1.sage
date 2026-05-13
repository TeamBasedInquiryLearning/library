v1 = vector([1,-1,2])
v2 = vector([1,2,1])

# illustrate set of two vectors

p = plot(v1,thickness=5)
p += plot(v2,thickness=5)
p=p.rotate([1,0,0],3*pi/4)
p
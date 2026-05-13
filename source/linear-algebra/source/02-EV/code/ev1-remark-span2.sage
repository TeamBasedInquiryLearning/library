v1 = vector([1,-1,2])
v2 = vector([1,2,1])


# illustrate the *span* 

p = plot([])
for _ in range(1000):
    a = randrange(-99,100)
    b = randrange(-99,100)
    p += plot(a*v1+b*v2, thickness=15)
p=p.rotate([1,0,0],3*pi/4)
p
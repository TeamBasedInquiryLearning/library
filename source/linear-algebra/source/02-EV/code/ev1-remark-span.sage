v1 = vector([1,-1,2])
v2 = vector([1,2,1])

# illustrate set of two vectors

p = plot(v1)
p += plot(v2)
show(p)

# illustrate the *span* that set

p = plot([])
for _ in range(1000):
    a = randrange(-99,100)
    b = randrange(-99,100)
    p += plot(a*v1+b*v2)
show(p)

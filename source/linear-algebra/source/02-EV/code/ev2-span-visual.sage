# create empty plot
p = plot([])

# define three vectors
v1 = vector([1,-1,0])
v2 = vector(FIXME)
v3 = vector(FIXME)

# do this 100 times
for _ in range(100):
    # choose random coefficients
    a = randrange(-9,10)
    b = randrange(-9,10)
    c = randrange(-9,10)
    # create linear combination
    linear_combo = a*v1 + b*v2 + FIXME
    # add it to the plot
    p += plot(linear_combo)

# show the plot
show(p)

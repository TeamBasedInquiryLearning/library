# create empty plot
p = plot([])

# do this 100 times
for _ in range(100):
    # pick random a value from -99 to 99
    a = randrange(-99,100)
    # pick random b value from -99 to 99
    b = randrange(-99,100)
    # plot random linear combination of two vectors based on a,b
    p += plot(a*vector([1,2])+b*vector([FIXME]))

# display plot
show(p)

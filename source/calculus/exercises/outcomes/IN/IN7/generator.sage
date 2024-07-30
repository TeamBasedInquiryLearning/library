class Generator(BaseGenerator):
    def data(self):
        x = var("x")
        z0 = randrange(1,6)*choice([-1,1])
        a = z0-randrange(1,6)
        b = z0+randrange(1,6)
        if choice([True,False]):
            z1 = b+randrange(1,6)
        else:
            z1 = a-randrange(1,6)
        f = expand(6*(x-z0)*(x-z1))
        return {
            "fx": f,
            "a": a,
            "b": b,
            "z": z0,
            "net": integral(f,x,a,b),
            "total": abs(integral(f,x,a,z0))+abs(integral(f,x,z0,b)),
        }
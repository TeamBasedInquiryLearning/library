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
        f = integrate(choice([-1,1])*6*(x-z0)*(x-z1),x) + \
            randrange(10,100)*choice([-1,1])
        return {
            "fx": f,
            "a": a,
            "fa": f(x=a),
            "b": b,
            "fb": f(x=b),
            "z": z0,
            "fz": f(x=z0),
            "min": min(f(x=a),f(x=b),f(x=z0)),
            "max": max(f(x=a),f(x=b),f(x=z0)),
            "ignored": z1,
            "fignored": f(x=z1),
        }
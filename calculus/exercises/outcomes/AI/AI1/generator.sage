class Generator(BaseGenerator):
    def data(self):
        a = randrange(-4,0)
        b = randrange(2,5)
        c = [choice([-1,1])*randrange(1,6) for _ in range(3)]
        favg = (c[0]*b+c[1]*b^2+c[2]*b^3-c[0]*a-c[1]*a^2-c[2]*a^3)/(b-a)

        return {
            "f": 3*c[2]*x^2+2*c[1]*x+c[0],
            "favg": favg,
            "a": a,
            "b": b,
            "b-a": b-a,
        }

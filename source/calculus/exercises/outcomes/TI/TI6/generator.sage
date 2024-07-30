class Generator(BaseGenerator):
    def data(self):
        x=var("x")

        rolls = range(2,10)
        rolls = [r*choice([-1,1]) for r in rolls]
        shuffle(rolls)
        a,b,c,d,A,B,C,D = rolls
        d=abs(d)

        f = ( C/(x-c)+D/(x^2+d^2) ).simplify_full()
        pf=f.partial_fraction()
        F=D/d*arctan(x/d)+C*log(abs(x-c))

        g = ( A/(x-a)+B/(x-b) ).simplify_full()
        pg=g.partial_fraction()

        return {
            "f": f,
            "pf": pf,
            "F": F,  
            "g": g,
            "pg": pg,
        }

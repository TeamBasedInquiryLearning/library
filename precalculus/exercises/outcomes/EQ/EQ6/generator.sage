class Generator(BaseGenerator):
    def data(self):
        eqs = []

        # generate rational equation with one solution
        if choice([True,False]):
            # e.g. 8/(x-3) = -6
            p,q,offset = [choice([-1,1])*i for i in sample(range(2,7), 3)]
            eq = CheckIt.shuffled_equation(
                (p+q*offset)/(x+offset),
                -q
            )
            eqs = [{
                "eq": eq,
                "sols": [{"sol": p/q}]
            }]
        else:     
            # e.g. 3 = 1/4 - 5/(2x)
            a,b,c,d,e = [choice([-1,1])*i for i in sample(range(2,7), 5)]
            eq = CheckIt.shuffled_equation(
                d/b-c/b,
                a/(e*x)
            ) + c/b
            eqs = [{
                "eq": eq,
                "sols": [{"sol": a*b/(c-d)/e}]
            }]

        # generate rational equation with two solutions
        # (x+6)/(x+2) - 1 = (x+5)/(x+7)
        # (x+6)(x+7) - (x+2)(x+7) = (x+5)(x+2)
        # x2+13x+42 - (x2+9x+14) = (x2+7x+10)
        # 0 = x2+3x-18
        # 0 = (x+6)(x-3)

        shuffle(eqs)
        return {
          "eqs": eqs
        }
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
        # h/t https://math.stackexchange.com/a/4950440
        while True:
            offset = choice([-1,1])
            a,b,d = [choice([-1,1])*(2*i+offset) for i in sample(range(1,4), 3)]
            e = 1
            g = d + choice([-1,1])
            c = d + e*(a+d)*(b+d)/(g-d)
            f = g + e*(a+g)*(b+g)/(g-d)
            if abs(c)<=12 and abs(f)<=12:
                break
        eq = CheckIt.shuffled_equation(
            (x+c)/(x+d),
            e,
            -(x+f)/(x+g)
        )
        eqs += [{
            "eq": eq,
            "sols": [{"sol": a},{"sol": b},],
            "d": d,
            "g": g,
            "c": c,
            "f": f,
        }]

        # generate rational equation with one solution
        a,b,f = [choice([-1,1])*i for i in sample(range(2,6), 3)]
        c = 1
        d = f + b*c
        e = b*d-a*f-a*b*c
        whatif_eq = (c + d/(x-a) + e/(x-a)/(x-b) == 0)
        whatif_simp = ((x-a)*(c*x+f)==0)
        whatif_explainer = choice([
            "explainA",
            "explainB",
            "explainC",
            "explainD",
        ])

        shuffle(eqs)
        return {
            "eqs": eqs,
            "whatif": {
                "eq": whatif_eq,
                "simp": whatif_simp,
                "sol": -f/c,
                "notsol": a,
                "notsol_term": x-a,
                whatif_explainer: True,
            }
        }
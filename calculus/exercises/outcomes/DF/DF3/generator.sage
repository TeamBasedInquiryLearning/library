class Generator(BaseGenerator):
    def data(self):
        xs=list(var("x y t w"))
        shuffle(xs)
        fns=list(var("f g h"))
        shuffle(fns)
        
        #polynomial
        ps = sample(list(range(1,7)),3)
        f = sum([randrange(1,10)*choice([-1,1])*xs[0]^p for p in ps]) + \
            randrange(1,10)*choice([-1,1])
        fs = [
            {
                "f":f,
                "fn":fns[0],
                "x":xs[0],
                "df":f.diff(),
            }
        ]
        
        #trig + transcendental
        trig = choice([cos,sin])
        transc = choice([log,exp])
        f = randrange(1,5)*choice([-1,1])*trig(xs[1]) + \
            randrange(1,5)*choice([-1,1])*transc(xs[1])
        fs += [
            {
                "f":f,
                "fn":fns[1],
                "x":xs[1],
                "df":f.diff(),
            }
        ]
        
        #fractional/negative powers
        coprimes = [3,4,5,7]
        a,b = sample(coprimes,2)
        radical = xs[2]^(b/a)
        radical_latex = LatexExpr(f"\\sqrt[{a}]{{{xs[2]}^{b}}}")
        frac = randrange(1,10)/xs[2]^randrange(2,6)
        frac_latex = latex(frac)
        f = radical+frac
        flatex = radical_latex + " + " + frac_latex
        fs += [
            {
                "f":flatex,
                "fn":fns[2],
                "x":xs[2],
                "df":f.diff(),
            }
        ]

        shuffle(fs)
        return {"fs":fs}
        
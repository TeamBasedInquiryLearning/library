class Generator(BaseGenerator):
    def data(self):
        x=var("x")
        y=var("y")
        t=var("t")
        w=var("w")
        f="f"
        g="g"
        h="h"
        
        index1 = randint(0, 3)
        index2 = randint(0, 3)
        index3 = randint(0, 3)
        
        listvars=[x,y,t,w]
        
        functionnames=[f,g,h]

        factors = [
            #   x^(randrange(2,10)*choice([-1,1])),
            #       x^(1/randint(2,10)*choice([-1,1])),
            e^x,
            cos(x),
            sin(x),
            log(x,e),
        ]

        shuffle(factors)
        shuffle(functionnames)

        coeffs = [randint(1,6)*choice([-1,1]) for _ in range(9)]
        polynomials=[coeffs[3*i]*x^2+coeffs[3*i+1]*x+coeffs[3*i+2] for i in range(3)]

        f1=factors[0]*polynomials[0]
        f2=choice([factors[1]/polynomials[1], polynomials[1]/factors[1]])
        f3=choice([x^(randrange(2,10)*(-1)), x^(1/randrange(2,10)*(-1))])*polynomials[2]

        f1a = f1()(x=listvars[index1])
        f2a = f2()(x=listvars[index2])
        f3a = f3()(x=listvars[index3])
        
        df1=f1a.diff()
        df2=f2a.diff()
        df3=(f3a.diff()).full_simplify()

        
        functions = [
            {"f":f1a,"dfdx":df1, "fn": functionnames[0], "v": listvars[index1]},
            {"f":f2a,"dfdx":df2, "fn": functionnames[1], "v": listvars[index2]},
            {"f":f3a,"dfdx":df3, "fn": functionnames[2], "v": listvars[index3]},
        ]
        shuffle(functions)
        

        return {
          "functions": functions,
        }


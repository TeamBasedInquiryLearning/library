class Generator(BaseGenerator):
    def data(self):
        x=var("x")
        y=var("y")
        t=var("t")
        w=var("w")
        f="f"
        g="g"
        h="h"
        k="k"

        listvars=[x,y,t,w]
        shuffle(listvars)

        functionnames=[f,g,h,k]
        shuffle(functionnames)

        polynomial=sum([randrange(1,6)*choice([-1,1])*x^i for i in range(3)])
        specials = [
            sin,
            cos
        ]
        shuffle(specials)
        fs = [choice([-1,1])*randrange(1,10)*specials[0](polynomial)]

        primes = [2,3,5,7]
        shuffle(primes)
        coeff=choice([-1,1])*randrange(2,10)
        fs.append(
            coeff*specials[1](x^(primes[0]/primes[1]))
        )
        fs.append(
            coeff*specials[1](x)^(primes[0]/primes[1])
        )
        
        fs.append(sum([
            randrange(1,6)*choice([-1,1])*e^x,
            randrange(1,6)*choice([-1,1])*x,
            randrange(1,6)*choice([-1,1]),
        ])^randrange(3,7))

        functions = [
            {
                "f":fs[i](x=listvars[i]),
                "dfdx":fs[i].diff()(x=listvars[i]),
                "fn": functionnames[i], 
                "v": listvars[i],
            }
            for i in range(len(fs))
        ]
        shuffle(functions)


        return {
        "functions": functions,
        }


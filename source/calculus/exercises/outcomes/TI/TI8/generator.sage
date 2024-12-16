class Generator(BaseGenerator):
    def data(self):
        from sage.symbolic.integration.integral import definite_integral

        x=var("x")
        tasks = []
       
        bs = sample([choice([-1,1])*n for n in range(2,10)],5)

        coeff = [2,3,4,5,6,7,8]

        case1 = choice([0,1])

        # converges with infinite bound
        if case1 == 0:
            p = randrange(3,10)
            q = randrange(3,10)
            bottom = bs[0] + randrange(1,6)
            shuffle(coeff)
            antidiff(x) = -1*(coeff[0]/coeff[1])/(x-bs[0])^(SR(p)/q)
            tasks.append({
                "integrand": antidiff(x).diff(x),
                "converges": True,
                "top": oo,
                "bottom": bottom,
                "proper": False,
                "improper": True,
                "int": 0-antidiff(bottom),
            })

        # diverges with infinite bound
        if case1 == 1:
            p = randrange(1,5)
            q = randrange(p+1,p+5)
            bottom = bs[1]+randrange(1,6)
            shuffle(coeff)
            antidiff(x) = choice([(coeff[0]/coeff[1])*(x-bs[1])^(SR(p)/q), (coeff[0]/coeff[1])*log(x-bs[1]) ])
            tasks.append({
                "integrand": antidiff(x).diff(x),
                "converges": False,
                "top": oo,
                "bottom": bottom,
                "proper": False,
                "improper": True,
                "int": r"\infty",
            })

        # converges with finite bounds
        if case1 == 1:
            case1 = randrange(0,2)
            p = randrange(1,5)
            q = randrange(p+1,p+5)
            top = bs[2]+randrange(1,6)
            shuffle(coeff)
            antidiff(x) = (coeff[0]/coeff[1])*(x-bs[2])^(SR(p)/q)
            tasks.append({
                "integrand": antidiff(x).diff(x),
                "converges": True,
                "top": top,
                "bottom": bs[2],
                "proper": False,
                "improper": True,
                "int": antidiff(top),
            })

        # diverges with finite bounds
        if case1 == 0:
            p = randrange(3,10)
            q = randrange(3,10)
            top = bs[3]+randrange(1,6)
            shuffle(coeff)
            antidiff(x) = choice([-1*(coeff[0]/coeff[1])/(x-bs[3])^(SR(p)/q), (coeff[0]/coeff[1])*log(x-bs[3]) ])
            tasks.append({
                "integrand": 1/(x-bs[3])^(SR(p)/q),
                "converges": False,
                "top": top,
                "bottom": bs[3],
                "proper": False,
                "improper": True,
                "int": r"\infty",
            })
        
        
        # proper
        p = randrange(3,10)
        q = randrange(3,10)
        bottom = bs[4]+randrange(1,6)
        top = bottom + randrange(1,6)
        tasks.append({
            "integrand": 1/(x-bs[4])^(SR(p)/q),
            "converges": True,
            "top": top,
            "bottom": bottom,
            "proper": True,
            "improper": False,
        })    

        shuffle(tasks)

        return {"tasks": tasks}
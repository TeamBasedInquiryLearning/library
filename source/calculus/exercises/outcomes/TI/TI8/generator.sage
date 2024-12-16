class Generator(BaseGenerator):
    def data(self):
        from sage.symbolic.integration.integral import definite_integral

        x=var("x")
        tasks = []
       
        bs = sample([choice([-1,1])*n for n in range(2,10)],5)


        case1 = 0

        # converges with infinite bound
        if case1 == 0:
            p = randrange(3,10)
            q = randrange(2,p)
            bottom = bs[0]+randrange(1,6)
            tasks.append({
                "integrand": 1/(x-bs[0])^(p/q),
                "converges": True,
                "top": oo,
                "bottom": bottom,
                "proper": False,
                "improper": True,
                "int": definite_integral( 1/(x-bs[0])^((p)/q), x, bottom, oo),
            })

        # diverges with infinite bound
        if case1 == 1:
            p = randrange(2,9)
            q = randrange(p+1,10)
            bottom = bs[1]+randrange(1,6)
            tasks.append({
                "integrand": 1/(x-bs[1])^((p)/q),
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
            p = randrange(2,9)
            q = randrange(p+1,10)
            top = bs[2]+randrange(1,6)
            tasks.append({
                "integrand": 1/(x-bs[2])^((p)/q),
                "converges": True,
                "top": top,
                "bottom": bs[2],
                "proper": False,
                "improper": True,
                "int": definite_integral( 1/(x-bs[2])^((p)/q), x, bs[2], top),
            })

        # diverges with finite bounds
        if case1 == 0:
            p = randrange(3,10)
            q = randrange(2,p)
            top = bs[3]+randrange(1,6)
            tasks.append({
                "integrand": 1/(x-bs[3])^((p)/q),
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
        tasks.append({
            "integrand": 1/(x-bs[4])^((p)/q),
            "converges": True,
            "top": bs[4]+randrange(1,6),
            "bottom": bs[4],
            "proper": True,
            "improper": False,
        })    

        shuffle(tasks)

        return {"tasks": tasks}
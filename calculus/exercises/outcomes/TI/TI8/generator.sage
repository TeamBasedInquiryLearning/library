class Generator(BaseGenerator):
    def data(self):
        x=var("x")
        tasks = []
       
        bs = sample([choice([-1,1])*n for n in range(2,10)],4)

        # converges with infinite bound
        p = randrange(3,10)
        q = randrange(2,p)
        tasks.append({
            "integrand": 1/(x-bs[0])^(SR(p)/q),
            "converges": True,
            "top": oo,
            "bottom": bs[0]+randrange(1,6),
        })

        # diverges with infinite bound
        p = randrange(2,9)
        q = randrange(p+1,10)
        tasks.append({
            "integrand": 1/(x-bs[1])^(SR(p)/q),
            "converges": False,
            "top": oo,
            "bottom": bs[1]+randrange(1,6),
        })

        # converges with finite bounds
        p = randrange(2,9)
        q = randrange(p+1,10)
        tasks.append({
            "integrand": 1/(x-bs[2])^(SR(p)/q),
            "converges": True,
            "top": bs[2]+randrange(1,6),
            "bottom": bs[2],
        })

        # diverges with finite bounds
        p = randrange(3,10)
        q = randrange(2,p)
        tasks.append({
            "integrand": 1/(x-bs[3])^(SR(p)/q),
            "converges": False,
            "top": bs[3]+randrange(1,6),
            "bottom": bs[3],
        })

        shuffle(tasks)

        return {"tasks": tasks}
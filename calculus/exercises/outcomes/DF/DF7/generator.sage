class Generator(BaseGenerator):
    def data(self):
        x,y = var("x y")

        # random list of variables, can be used more to create harder problems
        v = [x,y]
        shuffle(v)
        # random list of special functions   
        specials = [sin,cos,exp]
        shuffle(specials)
        # terms that will be used to build the equations
        terms = [
            randrange(1,10)*choice([-1,1])*y^randrange(3,6) + randrange(1,10)*choice([-1,1]),
            randrange(1,10)*choice([-1,1])*x^randrange(3,6) +  randrange(1,6)*choice([-1,1])*specials[0](y),
            randrange(1,6)*choice([-1,1])*specials[1](v[0])*v[1],
            randrange(1,6)*choice([-1,1])*specials[2](x),
        ]
        # to make one of the equations not require the product rule, "terms" is not shuffled
        # uncomment shuffle for possibly even harder problems
        #     shuffle(terms)
        equations = []

        for n in range(2):
            equation = CheckIt.shuffled_equation(
                *terms[2*n:2*n+2]
            )
        # terms[0:2] picks up element 0 and 1 of "terms"
        # terms[2:4] picks up element 2 and 3 of "terms"
            yp_top = -sum([terms[i].diff(x) for i in range(2*n,2*n+2)])
            yp_bot = sum([terms[i].diff(y) for i in range(2*n,2*n+2)])

            equations.append({
                "equation": equation,
                "yp": yp_top/yp_bot,
            })
        # first equation has two dy/dx terms that need to be taken on one side
        # second equation has only one dy/dx but requires product rule
        return {"equations":equations}

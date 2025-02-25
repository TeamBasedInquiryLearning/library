load("../../../source/common/sagemath/library.sage")

class Generator(BaseGenerator):
    def data(self):
        eqvar, ineqvar = sample([var('x'),var('y'),var('z')],2)

        a,b,c,d,f = sample([n*choice([-1,1]) for n in range(2,7)], 5)

        # ensure a*b-d != 0
        d = a*b + choice([-1,1])*randrange(2,6)

        LHS = b*eqvar+c
        RHS = d*eqvar+f

        solution_eq = (f-a*c)/(a*b-d)
        equation = choice([
            SR(a).mul(LHS, hold=True) == RHS,
            RHS == SR(a).mul(LHS, hold=True)
        ])


        a,b,c= sample([n*choice([-1,1]) for n in range(2,7)], 3)

        ## ensure |f-a*c| =< 15 (prevent big sols)
        f = a*c + randrange(-15,16)
        # ensure |a*b-d| >= 2 (prevent division by zero)
        d = a*b + choice([-1,1])*randrange(2,6)
        direction = choice(["left","right"])
        strict = choice([True,False])
        solution_ineq = (f-a*c)/(a*b-d)
        if direction == "left":
            if strict:
                interval_ineq = f"(-\\infty, {solution_ineq})"
                inequality = choice([
                    SR(a).mul(b*ineqvar+c,hold=True) < d*ineqvar+f,
                    d*ineqvar+f > SR(a).mul(b*ineqvar+c,hold=True)
                ])
            else:
                interval_ineq = f"(-\\infty, {solution_ineq}]"
                inequality = choice([
                    SR(a).mul(b*ineqvar+c,hold=True) <= d*ineqvar+f,
                    d*ineqvar+f >= SR(a).mul(b*ineqvar+c,hold=True)
                ])
        else:
            if strict:
                interval_ineq = f"({solution_ineq}, \\infty)"
                inequality = choice([
                    SR(a).mul(b*ineqvar+c,hold=True) > d*ineqvar+f,
                    d*ineqvar+f < SR(a).mul(b*ineqvar+c,hold=True)
                ])
            else:
                interval_ineq = f"[{solution_ineq}, \\infty)"
                inequality = choice([
                    SR(a).mul(b*ineqvar+c,hold=True) >= d*ineqvar+f,
                    d*ineqvar+f <= SR(a).mul(b*ineqvar+c,hold=True)
                ])


        return {
            "equation": equation,
            "solution_eq": solution_eq,
            "variable": eqvar,
            "solution_ineq": solution_ineq,
            "interval_ineq": interval_ineq,
            "inequality": inequality,
            "direction": direction,
            "strict": strict,
        }

    @provide_data
    def graphics(data):
        P = TBIL.numberline_plot()
        if data["direction"] == "left":
            P += TBIL.inequality_plot(
                end=data["solution_ineq"],
                strict_end=data["strict"],
                label_endpoints=True,
            )
        else:
            P += TBIL.inequality_plot(
                start=data["solution_ineq"],
                strict_start=data["strict"],
                label_endpoints=True,
            )
        P.axes(False)
        return {
            "plot": plot(P)
        }

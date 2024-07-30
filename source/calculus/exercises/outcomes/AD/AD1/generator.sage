class Generator(BaseGenerator):
    def data(self):
        # tangent
        x=var("x")
        
        numterms=randint(2,4)
        powers=[0,1,2,3,4]
        shuffle(powers)
        
        chosenpowers=[powers[i] for i in range(numterms)]
        
        chosenpowers=chosenpowers.sort()

        funcname=choice(["f", "g", "h"])


        poly(x)=0
        
        for i in range(numterms):
            poly(x)=poly(x)+randint(1,6 - i)*choice([1,-1])*x^(powers[i])
            
        polyexp=poly(x)
        
        a=randint(1,3)*choice([-1,1])
        fa=poly(a)

        dfdx(x)=poly(x).diff()

        slope=dfdx(x=a)

        tanline=slope*(x-a)+fa

        tanline=tanline.full_simplify()

        tangent = {
            "poly": polyexp,
            "function_symbol": funcname,
            "pointx": a,
            "pointy": fa,
            "tanline": tanline,
        }

        # motion
        t=var("t")
        position = sum([
                randrange(4-i,10-2*i)*choice([-1,1])*t^i
                for i in range(1,4)
            ])+randrange(1,9)*choice([-1,1])
        elapsed_time = randrange(1,4)
        units = choice(
            [
                "meters",
                "feet",
                "yards",
                "miles",
                "kilometers",
            ]
        )
        motion = {
            "position": position,
            "elapsed": {
                "time": elapsed_time,
                "position": position(t=elapsed_time),
                "displacement": position(t=elapsed_time)-position(t=0),
                "velocity": position.diff()(t=elapsed_time),
                "speed": abs(position.diff()(t=elapsed_time)),
                "acceleration": position.diff().diff()(t=elapsed_time),
            },
            "units": units,
        }

        # marginals
        x=var("x")
        price = randint(11,100)
        cost_function = sum([randint(1,10)*x^n for n in range(4)])
        marginal_cost = cost_function.diff()
        marginal_profit = price - marginal_cost
        widget = choice([
            "gadget",
            "widget",
            "gizmo",
        ])
        marginal = {
            "price": price,
            "cost_function": cost_function,
            "marginal_cost": marginal_cost,
            "marginal_profit": marginal_profit,
            "widget": widget,
        }

        return {
            "tangent": tangent,
            "motion": motion,
            "marginal": marginal,
        }
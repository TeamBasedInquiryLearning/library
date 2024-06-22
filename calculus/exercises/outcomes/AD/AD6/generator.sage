class Generator(BaseGenerator):
    def data(self):
        x = var("x")
        negative=choice([-1,1])
        def concavity_from_sign(sgn):
            if sgn<0:
                return "down"
            elif sgn>0:
                return "up"
            else:
                return "unknown"

        zeros = [
            -randrange(1,6),
            0,
            randrange(1,6),
        ]
        fpp = prod([x-z for z in zeros])*negative*randrange(3,6)
        f = integrate(integrate(fpp,x),x)
        data = [
            {
                "interval": f"(-\\infty, {zeros[0]} )",
                "concavity": concavity_from_sign(-negative),
            },
            {
                "point": zeros[0],
                "inflection": True,
            },
            {
                "interval": f"( {zeros[0]} , {zeros[1]} )",
                "concavity": concavity_from_sign(negative),
            },
            {
                "point": zeros[1],
                "inflection": True,
            },
            {
                "interval": f"( {zeros[1]} , {zeros[2]} )",
                "concavity": concavity_from_sign(-negative),
            },
            {
                "point": zeros[2],
                "inflection": True,
            },
            {
                "interval": f"( {zeros[2]} , \\infty )",
                "concavity": concavity_from_sign(negative),
            },
        ]
        fs = [
            {
                "f":f,
                "fpp":fpp,
                "data":data,
            }
        ]

        double_root = randrange(1,6)*choice([-1,1])
        fpp = x*(x-double_root)^2*negative*randrange(3,6)
        if double_root < 0:
            data = [
                {
                    "interval": f"(-\\infty, {double_root} )",
                    "concavity": concavity_from_sign(-negative),
                },
                {
                    "point": double_root,
                    "inflection": False,
                },
                {
                    "interval": f"( {double_root} , 0 )",
                    "concavity": concavity_from_sign(-negative),
                },
                {
                    "point": 0,
                    "inflection": True,
                },
                {
                    "interval": f"( 0, \\infty )",
                    "concavity": concavity_from_sign(negative),
                },
            ]
        else:
            data = [
                {
                    "interval": f"(-\\infty, 0 )",
                    "concavity": concavity_from_sign(-negative),
                },
                {
                    "point": 0,
                    "inflection": True,
                },
                {
                    "interval": f"( 0, {double_root} )",
                    "concavity": concavity_from_sign(negative),
                },
                {
                    "point": double_root,
                    "inflection": False,
                },
                {
                    "interval": f"( {double_root} , \\infty )",
                    "concavity": concavity_from_sign(negative),
                },
            ]
        f = integrate(integrate(fpp,x),x)
        fs.append(
            {
                "f":f,
                "fpp":fpp,
                "data":data,
            }
        )
        
        shuffle(fs)

        return {
            "fs": fs,
        }
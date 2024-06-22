class Generator(BaseGenerator):
    def data(self):
        t=var("t")

    #     powers=range(0,4)
    #     P=sample(powers,2)
    #     coeffs = [randint(1,10)*choice([-1,1]) for _ in range(2)]
    #     polynomial=coeffs[1]*t^P[1]+coeffs[0]*t^P[0]
        
    #     parts = [
    #         exp,
    #         log,
    #         csc,
    #         sec,
    #         cos,
    #         cot,
    #         arcsin,
    #         arctan,
    #     ]
    #     shuffle(parts)
        
        
        
    #     integrands = [
    #         randint(5,25)^polynomial,
    #         choice[randint(1,9)*choice([-1,1])*parts[0](parts[1](t)), randint(1,9)*choice([-1,1])*parts[0](polynomial*parts[1](t))],
    #         randint(1,6)*choice([-1,1])*parts[2](t)/parts[3](t),
    #         randint(1,8)*choise([-1,1])*parts[4]((parts[5](t)+randint(1,6)*choice([-1,1])*parts[6](t))/parts[7](t)),
    #     ]
    #     shuffle[integrands]

        options = [
            {
                "outs": [
                    randrange(1,10)*t^randrange(3,6),
                ],
                "ins": [
                    randrange(1,10)*cos(t)+randrange(1,10)*choice([-1,1]),
                    randrange(1,10)*sin(t)+randrange(1,10)*choice([-1,1]),
                    randrange(1,10)*exp(t)+randrange(1,10)*choice([-1,1]),
                    randrange(1,10)*log(t)+randrange(1,10)*choice([-1,1]),
                ]
            },
            {
                "outs": [
                    randrange(1,10)*exp(t),
                    randrange(1,10)*log(t),
                    randrange(1,10)*t^(-randrange(2,5)),
                ],
                "ins": [
                    randrange(1,10)*cos(t)+randrange(1,10)*choice([-1,1]),
                    randrange(1,10)*sin(t)+randrange(1,10)*choice([-1,1]),
                    t^randrange(3,6)+randrange(1,10)*choice([-1,1]),
                ]
            },
            {
                "outs": [
                    randrange(1,10)*sin(t),
                    randrange(1,10)*cos(t),
                ],
                "ins": [
                    randrange(1,10)*exp(t)+randrange(1,10)*choice([-1,1]),
                    randrange(1,10)*log(t)+randrange(1,10)*choice([-1,1]),
                    t^randrange(3,6)+randrange(1,10)*choice([-1,1]),
                ]
            },
        ]
        integrands = [
            choice(option["outs"])(t=choice(option["ins"]))
            for option in options
        ]
        shuffle(integrands)


        apol=randint(1,5)
        bpol=x
        answer1=integrands[0](t=x)*bpol.diff()
        functions=[
            {"function":integrands[0], "a":apol, "b":bpol,"answer":answer1}
        ]

        apol=randint(1,5)
        bpol=choice([x^randrange(2,5),exp(x),sin(x),cos(x)])+randrange(1,10)
        answer2=integrands[1](t=bpol)*bpol.diff()
        functions.append(
            {"function":integrands[1], "a":apol, "b":bpol,"answer":answer2}
        )

        apol=choice([x^randrange(2,5),exp(x),sin(x),cos(x)])+randrange(1,10)
        bpol=randint(1,5)
        answer3=-1*integrands[2](t=apol)*apol.diff()
        functions.append(
            {"function":integrands[2], "a":apol, "b":bpol,"answer":answer3}
        )
        
        apol=x
        bpol=randint(1,5)
        answer4=-1*integrands[2](t=apol)*apol.diff()
        functions.append(
            {"function":integrands[2], "a":apol, "b":bpol,"answer":answer4}
        )

    #     arad=randint(1,6)
    #     brad=randint(arad+1,8)
    #     answer2=integrands[1].integrate(x,arad,brad)
    #     functions.append(
    #         {"function":integrands[1], "a":arad, "b":brad,"answer":answer2}
    #     )

    #     atrig=choice([3,4,6])  #this choose a random bound from pi/3 pi/4 or pi/6
    #     btrig=choice([3,4,6])
    #     while btrig==atrig:  #this ensures a  is different than b 
    #         btrig=choice([3,4,6])
    #     k=choice([0,1,2,3])  #We are gonna pick a random quadrant
    #     atrig,btrig=pi/max(atrig,btrig)+k*pi/2,pi/min(atrig,btrig)+k*pi/2 #allows a and b to be in any quadrant
    #     answer3=integrands[2].integrate(x,atrig,btrig)
    #     functions.append(
    #         {"function":integrands[2], "a":atrig, "b":btrig,"answer":answer3}
    #     )

        shuffle(functions)

        return {
        "functions": functions
        }
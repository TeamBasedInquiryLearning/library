class Generator(BaseGenerator):
    def data(self):
        x=var("x")

        scenario = choice(["ladder","oilslick","shadow","car"])

        #ladder scenario
        if scenario=="ladder":
            ladderlength = randint(10,30)
            distancex = randint(1,ladderlength-2)
            velocityx= randint(1,6)

            distancey=sqrt(ladderlength^2-distancex^2)
            velocityy=-distancex*velocityx/distancey
            velyround=round(velocityy*1.0,2)
            numeratorladder=distancex*velocityx

            return {
                scenario: True,
                "ladderlength": ladderlength,
                "distancex": distancex,
                "velocityx": velocityx,
                "distancey": distancey,
                "numerator": numeratorladder,
                "velyround": velyround,
            }



        #oilslick scenario
        if scenario=="oilslick":
            radiusoil=randint(20, 100)
            dadt=randint(40, 90)
            denomoil=2*pi*radiusoil
            drdtround=round(dadt/denomoil,2)
            return {
                scenario: True,
                "radius": radiusoil,
                "dadt": dadt,
                "denomoil": denomoil,
                "drdtround": drdtround,
            }


        #shadow scenario
        if scenario=="shadow":
            disttolight = randint(2, 10)*5
            disttowall = randint(2, 10)*5
            lighttowall=disttolight+disttowall
            heightperson=round(uniform(4.8,6.5),1)
            personspeed=round(uniform(1,3),1)

            shadowdirection="up"
            persondirection=choice(["light", "wall"])
            if persondirection=="wall":
                shadowdirection="down"

            dHdtround=round(lighttowall*personspeed*heightperson/disttolight^2,2)
    #         numshadow=lighttowall*personspeed
    #         denomshadow=disttolight^2

            return {
                scenario: True,
                "disttolight": disttolight,
                "disttowall": disttowall,
                "heightperson": heightperson,
                "personspeed": personspeed,
                "persondirection": persondirection,
                "shadowdirection": shadowdirection,
                "dHdtround": dHdtround,
    #             "numshadow": numshadow,
    #             "denomshadow": denomshadow,
            }

        #car scenario
        if scenario=="car":
            d1=randint(2, 30)*5
            d2=randint(2, 30)*5
            s1=randint(6, 16)*5
            s2=randint(6, 16)*5

            v1=s1
            v2=s2

            direction1=choice(["east", "west"])
            direction2=choice(["north", "south"])

            if direction1=="west":
                v1=-1*s1

            if direction2=="south":
                v2=-1*s2
            distcar=sqrt(d1^2+d2^2)
            numcar=d1*v1+d2*v2
            dDdtround=round(numcar/distcar,2)

            return {
                scenario: True,
                "d1": d1,
                "d2": d2,
                "s1": s1,
                "s2": s2,
                "direction1": direction1,
                "direction2": direction2,
                "distcar": distcar,
                "numcar": numcar,
                "dDdtround": dDdtround,
            }
# TODO remove logic for IntIVP
class Generator(BaseGenerator):
    def data(self):
        def surd(var='x',a=2,b=1,):
            if len(var)>1:  #We put parentheses if var contains more than one term
                var="("+var+")"
            return r"\sqrt[%d]{%s^{%d}}" % (a,var,b)

        x=var("x")
        powers=range(0,5)
        P=sample(powers,3)
        coeffs = [randint(1,10)*choice([-1,1]) for _ in range(3)]
        polynomial=coeffs[2]*x^P[2]+coeffs[1]*x^P[1]+coeffs[0]*x^P[0]
        f     = [
            polynomial,
            choice([randint(2,10),1/randint(2,10)])*x^(choice([-randint(2,10),-1/randint(2,10)])),
            randint(1,11)*choice([e^x,
                                1/x,
                                cos(x),
                                sin(x)
                                ]),
            randint(1,6)*choice([
                    sec(x)^2,
                    sec(x)*tan(x),
                    csc(x)^2,
                    csc(x)*cot(x)
            ]),
        ]

        functions=[
            {"function":f[i],"answer":f[i].integrate(x)}
            for i in range(4)
        ]

        shuffle(functions)
        ##here we generate the IVP 
        powers2=range(0,3)
        P2=sample(powers2,2)
        coeffs = [randint(1,6)*choice([-1,1]) for _ in range(3)]
        polynomial=(P2[1]+1)*coeffs[1]*x^P2[1]+(P2[0]+1)*coeffs[0]*x^P2[0]
        const = randint(1,11)
        inpt = choice([-1,1])*randint(1,6)
        func(x) = polynomial.integrate(x)+const
        output=func(inpt)
    #    possnames = ['f','g','h','q','r'] #eventually it should be able to choose a function name from several, but my implementation was causing problems.
    #    name = choice(possnames)
        
        return {
        "functions": functions,
        "fdiff": polynomial,
    #      "name": name +'(x)',
        "IV": 'f(' +str(inpt)+')='+str(output),
        "answerB": func(x)
        }
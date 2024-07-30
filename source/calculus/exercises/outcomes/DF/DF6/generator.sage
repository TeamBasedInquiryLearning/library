# Compute derivatives using a combination of rules.
class Generator(BaseGenerator):
    def data(self):
        x=var("x")
        y=var("y")
        t=var("t")
        w=var("w")
        f="f"
        g="g"
        h="h"

        index1 = randint(0, 3)
        index2 = randint(0, 3)
        index3 = randint(0, 3)

        listvars=[x,y,t,w]
        shuffle(listvars) #function name index

        functionnames=[f,g,h]
        shuffle(functionnames) #function name index
        
        x1 = listvars[0]
        x2 = listvars[1]
        x3 = listvars[2]
        
        ## send exponent to xml file separately.  remember to differentiate f1^exp_f1
        exp = randint(3,6)
        frac = ((randint(1,6)*choice([-1,1])*x1^randint(1,6) + randint(1,6)*choice([-1,1]))/(randint(1,6)*choice([-1,1])*x1^randint(1,6) + randint(1,6)*choice([-1,1])))
        funcs = [
            {
                "fn": functionnames[0],
                "frac": frac,
                "dfrac": frac.diff(),
                "exp": exp,
                "exp_m1": exp-1,
                "x":x1,
                'foo':True,
            }
        ]
        
        trig = [
                cos(randint(1,6)*choice([-1,1])*x2^randint(2,4) + randint(1,6)*choice([-1,1])*x2^randint(0,1)),
                sin(randint(1,6)*choice([-1,1])*x2^randint(2,4) + randint(1,6)*choice([-1,1])*x2^randint(0,1)),
            ]
        shuffle(trig)
        f2 = sqrt(trig[0])
        funcs += [
            {
                "f": f2,
                "fn": functionnames[1],
                "x":x2,
                "df":f2.diff(),
            }
        ]
        
        exps = list(range(1,6))
        shuffle(exps)
        primes = [2,3,5,7]
        shuffle(primes)
        f3 = x3^(1/randint(2,4)) * (primes[0]*x3^exps[0] + primes[1]*choice([-1,1])*x3^exps[1])^randint(2,6)
        funcs += [
            {
                "f": f3,
                "fn": functionnames[2],
                "x":x3,
                "df":f3.diff(),
            }
        ]
        
        # df1_p1 = f1.diff()
        # df1 = f1_.diff()
        # df2 = f2.diff()
        # df3 = f3.diff()

        shuffle(funcs)
        return {
            "functions": funcs,
            # "f1": f1,
            # "exp_f1": exp_f1,
            # "f2": f2,
            # "f3": f3,
            # "xp": listvars[0],
            # "xe": listvars[1],
            # "xt": listvars[2],
            # "fn1": functionnames[0],
            # "fn2": functionnames[1],
            # "fn3": functionnames[2],
            # "df1":df1,
            # "exp_f1": exp_f1,
            # "exp_f1_": exp_f1 -1,
            # "df1_p1": df1_p1,
            # "df2":df2,
            # "df3":df3,
        }






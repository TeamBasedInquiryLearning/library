class Generator(BaseGenerator):
    def data(self):
        x=var("x")
        u=var("u")
        t=var("t")
        v=var("v")
        w=var("w")
        j="j"
        k="k"
        h="h"
        m="m"
        n="n"
        
        
        listvars=[x,u,t,v,w]
        shuffle(listvars)
        
        functionnames=[h,j,k,m,n]
        shuffle(functionnames)
        
        factors = [
            arctan,
            arcsin,
        ]
        
        f1 = log(choice([-1,1])*randrange(1,10)*factors[0](listvars[0])+choice([-1,1])*randrange(1,10)*factors[1](listvars[0]))
        
        f2 = factors[0]((choice([-1,1])*randrange(1,10)*listvars[1]))/log(choice([-1,1])*randrange(1,6)*listvars[1])
        
        f3 = choice([-1,1])*randrange(1,10)*factors[1](listvars[2])*ln(listvars[2]^randint(1,9)+choice([-1,1])*randrange(1,10))

        df1=f1.diff()
        df2=f2.diff()
        df3=f3.diff()
        
        functions = [
            {"f":f1,"dfdx":df1, "fn": functionnames[0], "v": listvars[0]},
            {"f":f2,"dfdx":df2, "fn": functionnames[1], "v": listvars[1]},
            {"f":f3,"dfdx":df3, "fn": functionnames[2], "v": listvars[2]},
        ]
        shuffle(functions)


        return {
            "functions": functions,
        }
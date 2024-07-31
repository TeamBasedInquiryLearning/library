class Generator(BaseGenerator):
    def data(self):
        n=var("n")
        
        
        
        #Exponential decreasing
        num=Integer(randint(1,5))
        denom=Integer(randint(num+1, num+5))
        coeff=randint(1,5)
        ratio=num/denom
        
        Converge1={
            "Sequence":coeff*(ratio)^n,
            "Limit":0,
            "Converge":True,
            "Bounded":True,
            "Mono":True,
        }
        
        # #Rational->0
        # denom=randint(1,5)
        # coeff=randint(1,5)
        
        # Converge2={
        #     "Sequence":coeff*n/(n^2+denom),
        #     "Limit":0,
        #     "Converge":True,
        #     "Bounded":True,
        #     "Mono":False,
        # }
        
        
        #Rational->c
        denom=randint(1,5)
        coeff=randint(1,5)
        
        Converge3={
            "Sequence":coeff*n^2/(n^2+denom),
            "Limit":coeff,
            "Converge":True,
            "Bounded":True,
            "Mono":True,
        }
        
        
        #Alt->0
        denom=randint(1,5)
        coeff=randint(1,5)
        
        Converge4={
            "Sequence":(-1)^n*coeff*n/(n^2+denom),
            "Limit":0,
            "Converge":True,
            "Bounded":True,
            "Mono":False,
        }
        
        
        #Exponential increase
        denom=Integer(randint(1,5))
        num=Integer(randint(denom+1, denom+5))
        coeff=randint(1,5)
        ratio=num/denom
        
        Diverge1={
            "Sequence":coeff*(ratio)^n,
            "Limit":oo,
            "Converge":False,
            "Bounded":False,
            "Mono":True,
        }
        
        #Rational->oo
        denom=randint(1,5)
        coeff=randint(1,5)
        
        Diverge2={
            "Sequence":coeff*n^3/(n^2+denom),
            "Limit":0,
            "Converge":False,
            "Bounded":False,
            "Mono":True,
        }
        
        
        #Alt->oo
        denom=randint(1,5)
        coeff=randint(1,5)
        
        Diverge3={
            "Sequence":(-1)^n*coeff*n^3/(n^2+denom),
            "Limit":0,
            "Converge":False,
            "Bounded":False,
            "Mono":False,
        }
        
        
        #Alt->c
        denom=randint(1,5)
        coeff=randint(1,5)
        
        Diverge4={
            "Sequence":(-1)^n*coeff*n^2/(n^2+denom),
            "Converge":False,
            "Bounded":True,
            "Mono":False,
        }
        
        Convergent=choice([Converge1, #Converge2, 
            Converge3, Converge4])
        
        Divergent=choice([Diverge1, Diverge2, Diverge3, Diverge4])
        
        
        
        
        
        
        
        Problems=[Convergent, Divergent]
        shuffle(Problems)

        return {
            "Problems": Problems,
        }

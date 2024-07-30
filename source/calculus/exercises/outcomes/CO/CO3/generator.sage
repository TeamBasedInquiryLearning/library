class Generator(BaseGenerator):
    def data(self):
        from sage.symbolic.integration.integral import definite_integral
        
        t=var("t")

        
        funct=[
            Integer(randint(1,5))*choice([-1,1])/Integer(randint(1,5))*t+Integer(randint(-5,5)),
            Integer(randint(1,5))*choice([-1,1])/Integer(randint(1,5))*Integer(randint(2,4))^t,
            Integer(randint(1,5))*choice([-1,1])*sin(t)+Integer(randint(1,5))*choice([-1,1]),
            Integer(randint(1,5))*choice([-1,1])*cos(t)+Integer(randint(1,5))*choice([-1,1]),
            Integer(randint(1,5))*choice([-1,1])/Integer(randint(1,5))*e^t,
            randint(1,3)*choice([-1,1])*t^choice([2,3])+randint(-3,3)*t+randint(-5,5)
        ]
        
        
        shuffle(funct)
        
        xt=funct[0]
        yt=funct[1]
        
        a=randint(-5,5)
        b=a+randint(3,10)
        
        xtd=diff(xt,t)
        ytd=diff(yt,t)
        
        
        name=choice(['r', 's','k', 'g', 'z', 'm', 'v', 'w'])
        
        
        

        return {
            "xt": xt,
            "yt": yt,
            "name": name,  
            "xtd": xtd,
            "ytd": ytd,
            "a": a,
            "b": b,  
        }

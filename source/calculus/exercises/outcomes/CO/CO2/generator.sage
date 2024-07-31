class Generator(BaseGenerator):
    def data(self):
        from sage.symbolic.integration.integral import definite_integral
        
        t=var("t")
        x=var("x")
        y=var("y")

        
        xp0=0
        
        while(xp0==0):    
            xt=randint(1,3)*choice([-1,1])*t^choice([2,3])+randint(-3,3)*t+randint(-5,5)
            yt=randint(1,3)*choice([-1,1])*t^choice([2,3])+randint(-3,3)*t+randint(-5,5)    
            t0=randint(-3,3)    
            xtd=diff(xt, t)
            ytd=diff(yt, t)    
            xtf(t)=xt
            ytf(t)=yt
            xtdf(t)=xtd
            ytdf(t)=ytd    
            x0=xtf(t0)
            y0=ytf(t0)    
            xp0=xtdf(t0)
            yp0=ytdf(t0)
        
        m=yp0/xp0
        
        tanline=m*(x-x0)+y0
        
        name=choice(['r', 's','k', 'g', 'z', 'm', 'v', 'w'])
        

        return {
            "xt": xt,
            "yt": yt,
            "t0": t0,
            "x0": x0,  
            "y0": y0,
            "xtd": xtd,
            "ytd": ytd,
            "tanline": tanline,
            "m": m, 
            "name": name,
        }

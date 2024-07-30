class Generator(BaseGenerator):
    def data(self):
        x=var("x")
        y=var("y")
        from sage.symbolic.integration.integral import definite_integral

        
        
        
        scenario=randint(0,3)
        
        if scenario==0:
            m=randint(1,6)/2
            b=randint(0,3)
            f(x)=m*x+b
            g(y)=(y-b)/m
            
        if scenario==1:
            m=randint(1,6)/2
            b=0
            f(x)=m*x^2+b
            g(y)=sqrt((y-b)/m)
            
        if scenario==2:
            m=randint(1,6)
            b=0
            f(x)=m*e^x+b
            g(y)=log((y-b)/m)
            
        if scenario==3:
            m=randint(1,6)
            b=randint(0,3)
            f(x)=sqrt(m*x+b)
            g(y)=(y^2-b)/m    
            
        
            
        
        
        a=randint(0,5)
        b=a+randint(1,4)
        
        low=f(a)
        high=f(b)
        
        
        
        
        
                        
        
                            
                            
        

        return {
            "f": f(x),
            "g": g(y),
            "a": a,
            "b": b,
            "low": low,
            "high": high,
        }

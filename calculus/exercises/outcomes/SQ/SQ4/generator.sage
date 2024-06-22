class Generator(BaseGenerator):
    def data(self):
        n=var("n")

        k=randint(1,3)
        
        c=randint(1,3)*choice([-1,1])
        
        I=randint(1,5)*choice([-1,1])
        
        a=randint(1,4)
        b=a+randint(1,4)
        r=1/b*a*choice([-1,1])
        
        limit1=c*(1)/(1-r)
        
        for i in range(k):
            limit1=limit1-c*r^i
            
        limit1=limit1+I    

        return {
            "c": c,  
            "k": k,
            "r": r,
            "I": I,
            "limit1": limit1,  
        }

class Generator(BaseGenerator):
    def data(self):        
        x=var("x")
        n=var("n")
        
        funct=choice(['power', 'exp'])
        
        a=Integer(randint(2,4))
        b=choice([-1,1])
        c=Integer(randint(1,3))
        d=Integer(randint(1,5))*choice([-1,1]) 
        
        if funct=='power':
            seq=d*b^n*n^c    
        if funct=='exp':
            seq=d*(b*a)^n     
            
            
            
        degree=randint(2,5)
        center=randint(-5,5)          
        
                
        poly=0          
        for i in range(degree+1):
                poly=poly+seq(n=i)/factorial(i)*(x-center)^i
        
        
        

        return {
            "a0": seq(n=0),
            "a1": seq(n=1),      
            "a2": seq(n=2),
            "a3": seq(n=3),      
            "a4": seq(n=4),
            "a5": seq(n=5),
            "a6": seq(n=6),      
            "degree": degree,
            "center": center,
            "seq": seq,
            "seq_frac":seq/factorial(n),
            "seq_term":(x-center)^n,
            "poly":poly,      
            
        }

class Generator(BaseGenerator):
    def data(self):
        from sage.symbolic.integration.integral import definite_integral
        
        x=var("x")
        n=var("n")

        a=1 #Integer(randint(1,3))*choice([-1,1])
        b=Integer(randint(-5,5))/choice([1,1,1,1,2,3,4,5])
        center=-1*b/a
        
        alt=choice([0,1])
        c=Integer(randint(1,3))/Integer(randint(1,3))
        
        num=c^n*(a*x+b)^n
        
        if alt==1:
            num=num*(-1)^n
            
            
        scenario=choice(['unbounded', 'harm', 'plain'])
        
        if scenario=='unbounded':
            denom=factorial(n)
            radius=oo
            leftsymb='('
            rightsymb=')'
        
        if scenario=='harm':
            denom=n
            radius=abs(1/(a*c))
            if alt==0:
                leftsymb='['
                rightsymb=')'
            if alt==1:
                leftsymb='('
                rightsymb=']'    
            
        if scenario=='plain':
            denom=1
            radius=abs(1/(a*c))
            leftsymb='('
            rightsymb=')'
            
        left=center-radius
        right=center+radius
        
        
        Sequence=num/denom
        
        #Randomize starting index
        #But make sure denominator isn't zero at starting index
        if denom==n:
            startIndex=choice([1,2])
        else:
            startIndex=choice([0,1,2])
        

        return {
            "Sequence": Sequence,
            "left": left,
            "right": right,
            "leftsymb": leftsymb,
            "rightsymb":rightsymb,
            "center":center,
            "radius":radius,  
            "startIndex": startIndex,
        }

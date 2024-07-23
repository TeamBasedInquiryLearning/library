class Generator(BaseGenerator):
    def data(self):
        var('x y')
        
        adjust = choice([0,1])
        
        n = 5 + adjust
        
        N=[1,2,3]
        shuffle(N)
        n1 = N[0]
        n2 = N[1]
        
        
        g(x) = x^(1+adjust) + randrange(1,6)
        
        q(x) = x^4 + randrange(1,5)*choice([-1,1])*x^n1 + randrange(1,5)*choice([-1,1])*x^n2 + randrange(1,5)*choice([-1,1])
        
        r(x) = randrange(1,6)*x^(adjust)*choice([-1,1]) + randrange(1,5)*choice([-1,1])
        
        while r(x) == 0:
            r(x) = randrange(1,6)*x^(adjust)*choice([-1,1]) + randrange(1,5)*choice([-1,1])
        
        f(x) = expand(r(x) + q(x)*g(x))
        
        
        
        
        
        
        
        return {
            "q": q(x),
            "r": r(x),
            "f": f(x),
            "g": g(x),
            
            
        }
            
           

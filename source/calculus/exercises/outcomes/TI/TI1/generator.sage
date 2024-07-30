class Generator(BaseGenerator):
    def data(self):
        #from sympy.calculus.singularities import singularities
        from sage.symbolic.integration.integral import definite_integral
        
        x = var("x")

        # define possible factors
        
        out(x)=0
        u(x)=0
        
        f=x
        
            
        while(out(x)==u(x) or derivative(f, x, 2)==0):
            outfactors = [
                x^randint(2,5),
                sqrt(x),
                log(abs(x)),
                e^x,
                cos(x),
                sin(x),
                1/sqrt(x),
            ]
            
            ufactors = [
                x^randint(2,5)+randint(-5,5),
                log(abs(x)),
                e^x,
                cos(x),
                sin(x),
            ]
            shuffle(outfactors)
            shuffle(ufactors)
            
            out(x)=outfactors[0]
            u(x)=ufactors[0]
        
            k=randint(1,5)*choice([-1,1])
        
        
            f=k*out(u(x))
        
        
        dfdx=f.diff()
        
        scenario=randrange(0,2)
        
        if scenario==0:
            n=randint(1,3)
            c=randint(2,5)
            k=randint(1,4)*choice([-1,1])
            g(x)=e^(c*x^n+k)*x^(n-1)
            a=randint(0,5)
            b=randint(a+1, a+4)
            defint=definite_integral(g(x),x,a,b)
            
        if scenario==1:
            bounds = [a*pi/2 for a in range(5)]
            a,b = sample(bounds,2)
            a,b = sorted([a,b])
            k = randrange(2,6)
            trig = choice([sin,cos])
            # u-sub is int_a^b trig(u)du
            primes = [2,3,5,7,11]
            shuffle(primes)
            c = primes[0]/primes[1]
            a,b=a/c,b/c
            
            g(x)=k*trig(c*x)
            defint=definite_integral(g(x),x,a,b)
            
        
        
        

        return {
            "f": f.simplify(),
            "dfdx": dfdx.simplify(),
            "g": g(x),
            "a": a,
            "b": b,
            "defint": defint,
        }

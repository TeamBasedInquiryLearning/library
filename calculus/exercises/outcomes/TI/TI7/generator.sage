class Generator(BaseGenerator):
    def data(self):
        import random # SB: this is needed for the c vs. d thing in partials
        
        x=var("x")

        
        #U-Sub
        out(x)=0
        u(x)=0
        
        while(out(x)==u(x) or derivative(out(u(x)), x, 2)==0):
            outfactors = [
                x^randint(2,5),
                sqrt(x),
                log(x),
                e^x,
                cos(x),
                sin(x),
                1/sqrt(x),
            ]
            
            ufactors = [
                x^randint(2,5)+randint(-5,5),
                log(x),
                e^x,
                cos(x),
                sin(x),
            ]
            out(x)=choice(outfactors)
            u(x)=choice(ufactors)

        k=randint(1,5)*choice([-1,1])        
        f=(k*out(u(x)))
        dfdx=(f.diff()).simplify()
        
        integrals=[{"integrand":dfdx, "method": 'Substitution'}]
        
        #Parts
        
        g=randint(1,5)*choice([-1,1])*choice([cos(x), sin(x), e^x])*x^(2*randint(0,3)+1)
        
        integrals+=[{"integrand":g, "method": 'Integration by parts'}]
        
        a=randint(1,5)*choice([-1,1])
        b=randint(1,5)*choice([-1,1])
        c, d = sample(range(-5, 5), 2)
        
        h=(a*(x-d)+b*(x-c))/((x-c)*(x-d))
        
        integrals+=[{"integrand":h, "method": 'Partial fractions'}]
        
        ftrig=choice([
                1/(x^2+randint(1,5)^2), #SB EDIT: used to be x, now is x^2
                sqrt(randint(1,5)^2-x^2),
                sqrt(x^2-randint(1,5)^2),
            ])
        
        integrals+=[{"integrand":ftrig, "method": 'Trigonometric substitution'}]
        
        shuffle(integrals)
        

        return {
            "integrals": integrals,
        }

class Generator(BaseGenerator):
    def data(self):
        from sage.symbolic.integration.integral import indefinite_integral
        from sage.symbolic.integration.integral import definite_integral

        x=var("x")

        
        
        vpfactors=[
            e^x,
            cos(x),
            sin(x),
        ]
        
        shuffle(vpfactors)
        vp(x)=vpfactors[0]
        
        k=randint(2,10)
        
        
        dfdx=x*vp(k*x)*randint(2,10)
        
        f=indefinite_integral(dfdx, x)
        
        a=randint(1,6)
        b=randint(a+1, a+5)
        
        fp(x)=dfdx
        
        defint=definite_integral(fp(x),x,a,b)

        
        

        return {
            "f": f.expand(),
            "dfdx": dfdx,
            "a": a,
            "b": b,
            "defint": defint,
        }

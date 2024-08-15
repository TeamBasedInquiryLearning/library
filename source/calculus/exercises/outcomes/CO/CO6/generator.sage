class Generator(BaseGenerator):
    def data(self):
        from sage.symbolic.integration.integral import definite_integral
        
        theta = var('t', latex_name=r"\theta")
        r=var("r")
        x=var("x")
        y=var("y")
        
        k=randint(1,5)

        
        functions=[
            randint(1,5)*theta^2+randint(0,5)*theta+randint(0,5),
            k*choice([-1,1])*sin(theta)+randint(0,5)+k,
            k*choice([-1,1])*cos(theta)+randint(0,5)+k,
        ]
        
        
        f=choice(functions)
        
        
        ang=[0, pi/6, pi/4, pi/3, pi/2, 2*pi/3, 3*pi/4, 5*pi/6, pi, 7*pi/6, 5*pi/4, 4*pi/3, 3*pi/2, 5*pi/3, 7*pi/4, 11*pi/6]
        
        i=randint(0,5)
        j=i+randint(2,6)
        a=ang[i]
        b=ang[j]
        
        

        return {
            "f": f,
            "a": a,
            "b": b,
        }

class Generator(BaseGenerator):
    def data(self):
        x=var("x")

        
        coeffs = [randint(1,6)*choice([-1,1]) for _ in range(4)]

        functions = [coeffs[0]/x^randint(1,3) , 
                    coeffs[1]*x^2 + coeffs[2]*x + coeffs[3] ]
        
    
        
        a = randint(1,10)*choice([1,-1])

        f = choice(functions)

        df = f.diff()
        
        dfa = f.diff()(x=a)

            

        return {
            "f": f,
            "dfdx": df,
            "dfdxa": dfa,
            "a": a,
        }
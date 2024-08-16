class Generator(BaseGenerator):
    def data(self):
        h=var("h")
        from sage.symbolic.integration.integral import definite_integral

        
        scenario = choice(["bucket","well"])
        
        if scenario=="bucket":
            height=randint(4,8)*5
            bucket=randint(2,5)*5+5*e^(-1*randint(1,20)/10*h)
            work=bucket*98/10
            return {
                scenario: True,
                "height": height,
                "bucket": bucket,
            }
        
        if scenario=="well":
            height=randint(4,8)*5
            radius=randint(2,5)
            return {
                scenario: True,
                "height": height,
                "radius": radius,
            }
        
        
            
            
    
    
    
    

                    
    
                         
                         
    

    


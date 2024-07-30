class Generator(BaseGenerator):
    def data(self):
        h=var("h")
        from sage.symbolic.integration.integral import definite_integral

        
        scenario = choice(["dam"])
        
        
        if scenario=="dam":
            height=randint(4,8)*5
            bottom=randint(5,10)*5
            top=randint(10,15)*5
            width=bottom+(top-bottom)*(1-h/height)
            force=width*62.4*h
            return {
                scenario: True,
                "height": height,
                "bottom": bottom,
                "top": top,
                "width": width,
                
            }
            
            
    
    
    
    

                    
    
                         
                         
    

    


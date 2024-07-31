class Generator(BaseGenerator):
    def data(self):
        h=var("h")
        from sage.symbolic.integration.integral import definite_integral

        
        unit=choice(["feet", "meters"])
        
        if unit=="feet":
            symbol="ft"
        if unit=="meters":
            symbol="m"    
        
        d(h)=randint(10, 30)/20*h+randint(1,5)
        
        scenario=randint(0,3)
        
        if scenario==0:
            solid="rectangular prism"
            base="sqaure"
            measuretype="side length"
            b=randint(5,10)
            height=randint(1,5)*5
            A(h)=b^2
            
            
        if scenario==1:
            solid="cylinder"
            base="circular"
            measuretype="radius"
            b=randint(2,6)
            height=randint(1,5)*5
            A(h)=pi*b^2
            
        if scenario==2:
            solid="pyramid"
            base="square"
            measuretype="side length"
            b=randint(5,10)
            height=randint(1,5)*5
            A(h)=(b*(1-h/height))^2
            
        if scenario==3:
            solid="cone"
            base="circular"
            measuretype="radius"
            b=randint(2,6)
            height=randint(1,5)*5
            A(h)=pi*(b*(1-h/height))^2
        

        return {
            "solid": solid,
            "base": base,
            "measuretype": measuretype,
            "b": b,
            "height": height,
            "unit": unit,  
            "A": A(h),
            "d": d(h),
            "symbol": symbol,  
        }


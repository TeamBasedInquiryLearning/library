class Generator(BaseGenerator):
    def data(self):
        digits = sample(range(1,7),5)
        digits = [choice([-1,1])*z for z in digits]
        g = (x-digits[0])*(x-digits[1])
        r = x-digits[2]
        q = digits[4]*(x-digits[3])
        f = q*g+r
        
        return {
            "f": f.expand(),
            "g": g.expand(),
            "q": q.expand(),
            "r": r.expand(),
        }
            
           

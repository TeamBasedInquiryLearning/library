class Generator(BaseGenerator):
    def data(self):
        var('x y')
        
        sign = choice([-1, 1])
        
        roottypes = ["none", "one", "two"]
        root = choice(roottypes)
        
        r1 = 0
        r2 = 0
        minx = 0
        maxx = 0
        
        R = [-5,-4,-3,-2,-1,1,2,3,4,5]
        
        q(x) = x
        
        if root == "none":
            a = randrange(1,6)
            b = randrange(-5,6)
            c = ceil(b^2/(4*a)) + randrange(1,6)
            minx =-1*b/(2*a)-3
            maxx =-1*b/(2*a)+3
            
        
        if root == "one":
            a = randrange(1,6)
            r1 = randrange(1, 6)*choice([-1,1])
            r2 = r1
            b = -1*a*2*(r1)
            c = a*r1^2
            minx = r1 - 3
            maxx = r1 + 3
        
        if root == "two":
            a = randrange(1,6)
            shuffle(R)
            r1 = R[0]
            r2 = R[1]
            b = -1*a*(r1+r2)
            c = a*r1*r2
            minx = min(r1, r2)-1
            maxx = max(r1, r2)+1
        
        a = sign*a
        b = sign*b
        c = sign*c
        
        q(x) = a*x^2 + b*x + c
        
        h = -1*b/(2*a)
        k = q(h)
        
        
        extrema = "something"
        face = "doesnt"
        
        if sign >0:
            face = "upwards"
            extrema = "minimum"
            
        else:
            face = "downwards"
            extrema = "maximum"
        
        
        
        
        
        return {
            root:True,
            "q": q(x),
            "h": h,
            "k": k,
            "c": c,
            "r1": r1,
            "r2": r2,
            "extrema": extrema,
            "face": face,
            "minx": minx,
            "maxx": maxx,
            "type":root,
            
            
        }
        
    @provide_data
    def graphics(data):
        a = data['minx']
        b = data['maxx']
        f(x) = data['q']
        r1 = data['r1']
        r2 = data['r2']
        h = data['h']
        k = data['k']
        root = data['type']
        
        
        f2 = f(r2)
        f1 = f(r1)
    # updated by clontz
    
    
        if root == "none": 
            return {"plot": plot(f(x), (a,b))+point((h,k), color='red', size=22) ,
               }
        
        if root == "one": 
            return {"plot": plot(f(x), (a,b))+point((h,k), color='red', size=22) +point((r1,f1), color='purple', size=22) ,
               }    
        
        if root == "two": 
            return {"plot": plot(f(x), (a,b))+point((h,k), color='red', size=22) +point((r1,f1), color='purple', size=22) +point((r2,f2), color='purple', size=22) ,
               }    
            
           
